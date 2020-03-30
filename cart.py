import json
import os


def main():
    with open('session_data/surfer.json') as surfer_json:
        current_user = json.load(surfer_json)[1]

    os.system('xdg-open ./' + current_user)


if __name__ == '__main__':
    main()

