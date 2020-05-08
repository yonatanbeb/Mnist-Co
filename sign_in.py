""" sign in to command line interface with profile """
import argparse
import json
import os


def main():
    # receive arguments from the command line
    parser = argparse.ArgumentParser()
    # argument 1: users' Username
    parser.add_argument('Username', type=str)
    # argument 2: users' Password
    parser.add_argument('Password', type=str)

    with open('session_data/profiles.json') as profiles_json:
        profiles = json.load(profiles_json)

    # list of arguments passed
    args = parser.parse_args()

    authorized = False
    # if profile with entered Username exists
    if args.Username in profiles:
        # if Password is wrong
        authorized = profiles[args.Username][0] == args.Password
        if not authorized:
            print('Incorrect Password')
    else:
        print('Profile not in system')

    # if user exists and password is correct
    if authorized:
        # update current user
        current_clearance_level = profiles[args.Username][1]
        current_user = args.Username
        # add users' Username to prompt
        os.system('echo "$(tput setaf 196)mnist&Co@ $(tput setaf 202)' + args.Username + ': $(tput setaf 178)" > '
                                                                                         './session_data/prompt')
    # otherwise -- sign in as guest
    else:
        current_clearance_level = 'No Clearance'
        current_user = 'Guest'
        os.system('echo "$(tput setaf 196)mnist&Co@ $(tput setaf 202)' + current_user +
                  ' : $(tput setaf 178)" > ./session_data/prompt')

    # update surfer.json
    surfer_json = json.dumps([current_clearance_level, current_user])
    with open('session_data/surfer.json', 'w') as surfer:
        surfer.write(surfer_json)


if __name__ == '__main__':
    main()
