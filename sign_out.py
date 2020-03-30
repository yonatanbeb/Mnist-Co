import json
import os


def main():
    current_clearance_level = 'No Clearance'
    current_user = 'Guest'

    surfer_json = json.dumps([current_clearance_level, current_user])
    with open('session_data/surfer.json', 'w') as surfer:
        surfer.write(surfer_json)

    os.system('echo "$(tput setaf 196)mnist&Co@ $(tput setaf 202)' + current_user +
              ' : $(tput setaf 178)" > ./session_data/prompt')


if __name__ == '__main__':
    main()
