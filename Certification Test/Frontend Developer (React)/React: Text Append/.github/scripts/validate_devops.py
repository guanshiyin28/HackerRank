import requests
import json
import sys
import time
import os

OS_MAP = {
    "ubuntu": "ubuntu22",
    "ubuntu18": "ubuntu22",
    "ubuntu22": "ubuntu22",
    "rhel7": "rhel8",
    "rhel8": "rhel8",
    "redhat": "redhat",
    "agnostic": "agnostic",
}

TARGET_OS = set(OS_MAP.values())
SOLUTION_VALIDATION = False

SESSION = requests.session()
SESSION.headers.update(
    {
        "Authorization": f"Bearer {os.environ['HACKERRANK_TOKEN']}",
        "cache-control": "no-cache",
        "content-type": "application/json",
    }
)

BASE_URL = "https://www.hackerrank.com/x/api/v1"


def question_exists(qid):
    print("finding question in company library...")

    tag_to_search = f"{qid}-solution" if SOLUTION_VALIDATION else f"{qid}"

    library_url = f"{BASE_URL}/library?limit=1&library=personal_all&tags={tag_to_search},duplicate"
    response = SESSION.request("GET", library_url)

    if response.status_code != 200:
        raise Exception("Failed to find question")

    data = response.json()

    if len(data["model"]["questions"]) != 0:
        return True, data["model"]["questions"][0]

    return False, None


def create_question():
    create_url = f"{BASE_URL}/questions"
    qid = sys.argv[1].split("-")[0]
    name = f"{qid} solution" if SOLUTION_VALIDATION else qid # use repo name as question name
    sudorank_os = os.environ.get("SUDORANK_OS", None)

    if not sudorank_os:
        raise Exception("SUDORANK_OS not set")

    print(f'creating question with name "{name}" and os "{sudorank_os}"')

    response = SESSION.request(
        "POST",
        create_url,
        data=json.dumps(
            {
                "type": "sudorank",
                "role_type": "devops",
                "custom_testcase_allowed": "True",
                "version": 3,
                "name": f"Copy of {name}",
                "sudorank_v3": True,
                "recommended_duration": 5,
                "sudorank_os": sudorank_os,
                "sudorank_context": "root",
            }
        ),
    )

    if response.status_code != 200:
        raise Exception("Failed to create question")

    data = response.json()

    return data["model"]


def clone_question(qid):
    print("cloning question...")

    clone_url = f"{BASE_URL}/questions/clone"
    name = f"{qid} solution" if SOLUTION_VALIDATION else qid
    payload = json.dumps(
        {
            "id": qid,
            "name": f"Copy of {name}",
        }
    )
    response = SESSION.request("POST", clone_url, data=payload)

    if response.status_code != 200:
        raise Exception("Failed to clone question")

    data = response.json()

    return data["question"]


def read_file(script_name):
    repo_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
    file_path = f"{repo_dir}/{script_name}.sh"
    if not os.path.exists(file_path):
        return ""

    return open(file_path, "r").read()


def solution_script_for_ubuntu(solution):
    return f"""cat <<"EOF" > /tmp/solve.sh
{solution}
EOF
/bin/su -c "bash /tmp/solve.sh" - ubuntu
"""


def get_devops_scripts(target_os):
    global SOLUTION_VALIDATION

    script_names = ["setup", "check", "solve", "cleanup"]
    scripts = {script_name: read_file(script_name) for script_name in script_names}

    if SOLUTION_VALIDATION:
        # TODO: add user based solution execution for other os as well
        if target_os == "ubuntu22":
            scripts["solve"] = solution_script_for_ubuntu(scripts["solve"])
        scripts["check"] = "({solve}) && ({check})".format(
            solve=scripts["solve"], check=scripts["check"]
        )

    return scripts


def get_target_os(sudorank_os):
    if not OS_MAP.get(sudorank_os, None):
        raise Exception("Target os not found")

    return OS_MAP[sudorank_os]


def update_question(question, qid):
    sudorank_os = question.get("sudorank_os", None) or question.get(
        "sudorank_draft", {}
    ).get("sudorank_os")

    print(f"update question...{question['id']}..cloned..{sudorank_os}")

    original_tags = question["visible_tags_array"]
    tag_to_add = f"{qid}-solution" if SOLUTION_VALIDATION else f"{qid}"

    if tag_to_add not in original_tags:
        original_tags.extend([tag_to_add, "duplicate"])

    target_os = get_target_os(sudorank_os)

    update_url = f"{BASE_URL}/questions/{question['id']}"

    payload = json.dumps(
        {
            "visible_tags_array": original_tags,
            "sudorank_os": target_os,
            "sudorank_scripts": {
                "language": "bash",
                **get_devops_scripts(target_os),
            },
        }
    )
    print(f"payload {payload}")
    response = SESSION.request("PUT", update_url, data=payload)
    if response.status_code != 200:
        raise Exception("Failed to update cloned question")

    if not os_updated(response.json()):
        print("Cloned question still have old os, retrying")
        response = SESSION.request("PUT", update_url, data=payload)

        if not os_updated(response):
            raise Exception("Cloned question still have old os")


def os_updated(data):
    sudorank_draft = data["model"]["sudorank_draft"]
    print(f"sudorank_draft {sudorank_draft}")

    target_os = sudorank_draft["sudorank_os"]
    print(f"Cloned question os {target_os}")
    return target_os in TARGET_OS


def validate_question(question):
    print("validating question...")
    validate_url = f"{BASE_URL}/questions/{question['id']}/validate_sudorank"

    response = SESSION.post(validate_url)
    print(f"validate response {response.content}")

    if response.status_code != 200:
        raise Exception("Failed to start validation...")

    return response.json()["task_id"]


def check_validation_status(task_id):
    print("polling on validation task with id", task_id)
    poll_url = f"{BASE_URL}/delayed_tasks/{task_id}/poll"

    while True:
        time.sleep(5)
        response = SESSION.get(poll_url)

        if response.status_code != 200:
            raise Exception(
                "Failed to get validation status", response.status_code, response.text
            )

        data = response.json()
        if (
            data["status_code"] == 2
            or data["response"]["additional_data"]["valid"] == True
        ):
            print(data)
            return data


def process_validator_response(validator_response):
    print("processing validator response...")
    if not validator_response["valid"]:
        for step, value in validator_response["data"].items():
            if value["valid"] == False:
                print(step, value)
                raise Exception(value["error"])

    print("validated successfully")

    scoring_output = validator_response["data"]["validate_scoring_output"]

    if SOLUTION_VALIDATION and not scoring_output["details"]:
        raise Exception("scoring output details is empty")

    if scoring_output["details"]:
        score = scoring_output["details"]["scoring_data"]["score"]
        print("scoring output is")
        print(scoring_output)
        print(f"score is {score}")
        if SOLUTION_VALIDATION and score != 1:
            raise Exception("Did not get full score")
        if not SOLUTION_VALIDATION and score != 0:
            raise Exception("Got full or partial score in question")


def main(solution=False):
    global SOLUTION_VALIDATION
    global SESSION

    try:
        # id of original question from library
        qid = sys.argv[1].split("-")[0]
        print(f"detected qid is {qid}")

        if not qid.isdigit():
            raise Exception("Could not parse Question ID")

        SOLUTION_VALIDATION = solution

        if SOLUTION_VALIDATION:
            print(f"Doing *****SOLUTION***** Validation")
            SESSION.headers.update(
                {"Authorization": f"Bearer {os.environ['SOLUTION_TOKEN']}"}
            )

        # get clone of question if exists
        exists, question = question_exists(qid)

        if not exists:
            try:
                question = clone_question(qid)
            except Exception as e:
                print(e)  # create question if clone fails
                question = create_question()

        print("question copy has id", question["id"])
        update_question(question, qid)
        task_id = validate_question(question)
        validator_response = check_validation_status(task_id)
        process_validator_response(validator_response["response"])
    except Exception as e:
        print(e)
        os._exit(1)


if __name__ == "__main__":
    main(solution=False)
    main(solution=True)
