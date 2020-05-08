""" opens User's cart directory containing all GRAB requests """
import json
import os


def main():
    # get current user's username
    with open('session_data/surfer.json') as surfer_json:
        current_user = json.load(surfer_json)[1]

    # open user's directory (only opens if such directory exists)
    os.system('xdg-open ./' + current_user)


if __name__ == '__main__':
    main()

