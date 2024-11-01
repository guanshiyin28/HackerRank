import requests
import json
import sys
from http.cookies import SimpleCookie
import time
import os
import logging

logging.basicConfig(level=logging.DEBUG)

STACKS = json.loads(os.environ['HACKERRANK_STACKS'])
TARGET_STACK = os.environ['TARGET_STACK']
TARGET_STACKS = set(STACKS.values())
SOLUTION_VALIDATION = False

SESSION = requests.session()
SESSION.headers.update({
    "Authorization": f"Bearer {os.environ['HACKERRANK_TOKEN']}",
    "cache-control": "no-cache",
    "content-type": "application/json",
})

BASE_URL = "https://www.hackerrank.com/"


def question_exists(qid):
    print('finding question in company library...')

    tag_to_search = f"{qid}-solution" if SOLUTION_VALIDATION else f"{qid}"

    library_url = BASE_URL + f"x/api/v1/library?limit=1&library=personal_all&tags={tag_to_search},duplicate"
    response = SESSION.request("GET", library_url)

    if response.status_code != 200:
        raise Exception("Failed to find question")

    data = response.json()

    if len(data['model']['questions']) != 0:
        return True, data['model']['questions'][0]

    return False, None


def clone_question(qid):
    print('cloning question...')

    clone_url = BASE_URL + "x/api/v1/questions/clone"
    payload = json.dumps({
        "id": qid,
        "name": f"Copy of {str(qid) + ' solution' if SOLUTION_VALIDATION else qid }"
    })
    response = SESSION.request("POST", clone_url, data=payload)

    if response.status_code != 200:
        raise Exception("Failed to clone question")

    data = response.json()

    return data['question']


def get_target_subtype(question):
    if TARGET_STACK != 'based_on_current_stack':
        return TARGET_STACK

    if not STACKS.get(question["sub_type"]):
        raise Exception("Target sub type not found")

    return STACKS[question["sub_type"]]


def update_question(question, qid):
    print(f"update question...{question['id']}..cloned..{question['sub_type']}")

    original_tags = question['visible_tags_array']
    tag_to_add = f"{qid}-solution" if SOLUTION_VALIDATION else f"{qid}"

    if question["sub_type"] == "custom_vm" and ".NET" in original_tags:
        question["sub_type"] = "dotnet3"

    if tag_to_add not in original_tags:
        original_tags.extend([tag_to_add, "duplicate"])
    elif question["sub_type"] in TARGET_STACKS:
        print('question already updated')
        return

    target_sub_type = get_target_subtype(question)

    update_url = BASE_URL + f"x/api/v1/questions/{question['id']}"

    payload = json.dumps({
        "visible_tags_array": original_tags,
        "sub_type": target_sub_type
    })
    print(f"payload {payload}")
    response = SESSION.request("PUT", update_url, data=payload)

    if not sub_type_updated(response):
        print("Cloned question still have old subtype, retrying")
        response = SESSION.request("PUT", update_url, data=payload)

        if not sub_type_updated(response):
            raise Exception("Cloned question still have old subtype")


def sub_type_updated(response):
    if response.status_code != 200:
        raise Exception("Failed to update cloned question")

    data = response.json()
    sub_type = data['model']['sub_type']

    print(f"Cloned question subtype {sub_type}")
    return sub_type in TARGET_STACKS


def update_project_zip(question):
    print('updating project zip...')
    update_url = BASE_URL + f"x/api/v1/questions/{question['id']}/upload"
    files = [
        ('source_file', ('project.zip', open('project.zip', 'rb'), 'application/zip'))
    ]
    del SESSION.headers['content-type']
    response = SESSION.post(update_url, files=files, data={'a': 1})

    if response.status_code != 200:
        print(response.status_code)
        raise Exception("Failed to update project zip")

    SESSION.headers.update({'content-type': 'application/json'})


def validate_question(question):
    print('validating question...')
    validate_url = BASE_URL + f"x/api/v1/questions/{question['id']}/validate_fullstack"

    response = SESSION.post(validate_url)

    if response.status_code != 200:
        raise Exception("Failed to start validation...")

    return response.json()['task_id']


def check_validation_status(task_id):
    print('polling on validation task with id', task_id)
    poll_url = BASE_URL + f"x/api/v1/delayed_tasks/{task_id}/poll"

    while True:
        time.sleep(5)
        response = SESSION.get(poll_url)

        if response.status_code != 200:
            raise Exception("Failed to get validation status", response.status_code, response.text)

        data = response.json()
        if data['status_code'] == 2 or data['response']['additional_data']['valid'] == True:
            print(data)
            return data


def process_validator_response(validator_response):
    print('processing validator response...')
    if not validator_response['valid']:
        for step, value in validator_response['data'].items():
            if value['valid'] == False:
                print(step, value)
                raise Exception(value['error'])

    print("validated successfully")

    scoring_output = validator_response['data']['validate_scoring_output']

    if SOLUTION_VALIDATION and not scoring_output['details']:
        raise Exception('scoring output details is empty')

    if scoring_output['details']:
        score = scoring_output['details']['scoring_data']['score']
        print("scoring output is")
        print(scoring_output)
        print(f"score is {score}")
        if SOLUTION_VALIDATION and score != 1:
            raise Exception('Did not get full score')
        if not SOLUTION_VALIDATION and score != 0:
            raise Exception('Got full or partial score in question')


def main(solution=False):
    global SOLUTION_VALIDATION
    global SESSION

    try:
        # id of original question from library
        qid = sys.argv[1].split('-')[0]
        print(f"detected qid is {qid}")

        if not qid.isdigit():
            raise Exception('Could not parse Question ID')

        # solution validation from args
        branch_name = sys.argv[2] if len(sys.argv) == 3 else ""
        print(f"detected branch name is {branch_name}")

        SOLUTION_VALIDATION = solution or "solution" in branch_name
        if SOLUTION_VALIDATION:
            print(f"Doing *****SOLUTION***** Validation")
            SESSION.headers.update({
                "Authorization": f"Bearer {os.environ['SOLUTION_TOKEN']}"
            })

        # get clone of question if exists
        exists, question = question_exists(qid)

        if not exists:
            question = clone_question(qid)
        print('question copy has id', question['id'])
        update_question(question, qid)
        update_project_zip(question)
        task_id = validate_question(question)
        validator_response = check_validation_status(task_id)
        process_validator_response(validator_response['response'])
    except Exception as e:
        print(e)
        os._exit(1)


if __name__ == "__main__":
    main()
