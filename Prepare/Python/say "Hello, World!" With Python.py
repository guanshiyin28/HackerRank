import sys

if __name__ == "__main__":
    message: str = "hello world"
    for letter in ", ".join(
        list(map(lambda word: word.capitalize(), (message + "!").split(" ")))
    ):
        sys.stdout.write(letter)
    sys.stdout.flush()
    sys.exit(0)
