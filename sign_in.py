import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Username', type=str)
    parser.add_argument('Password', type=str)

    with open('session_data/profiles.json') as profiles_json:
        profiles = json.load(profiles_json)

    args = parser.parse_args()

    authorized = False
    if args.Username in profiles:
        authorized = profiles[args.Username][0] == args.Password
        if not authorized:
            print('Incorrect Password')
    else:
        print('Profile not in system')

    if authorized:
        current_clearance_level = profiles[args.Username][1]
        current_user = args.Username
        os.system('echo "$(tput setaf 196)mnist&Co@ $(tput setaf 202)' + args.Username + ': $(tput setaf 178)" > '
                                                                                         './session_data/prompt')
    else:
        current_clearance_level = 'No Clearance'
        current_user = 'Guest'
        os.system('echo "$(tput setaf 196)mnist&Co@ $(tput setaf 202)' + current_user +
                  ' : $(tput setaf 178)" > ./session_data/prompt')

    surfer_json = json.dumps([current_clearance_level, current_user])
    with open('session_data/surfer.json', 'w') as surfer:
        surfer.write(surfer_json)


if __name__ == '__main__':
    main()
