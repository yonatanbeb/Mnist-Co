""" create Mnist&Co command line interface profile with clearance level """
import argparse
import json


def main():
    # receive arguments from the command line
    parser = argparse.ArgumentParser()
    # argument 1: requested Username
    parser.add_argument('Username', type=str)
    # argument 2: your Password
    parser.add_argument('Password', type=str)
    # argument 3: your user's Clearance Level
    parser.add_argument('clearance_level', type=int, choices=[0, 1])

    with open('session_data/profiles.json') as profiles_json:
        profiles = json.load(profiles_json)

    # list of the arguments passed
    args = parser.parse_args()

    # if user does not yet exist
    if args.Username not in profiles:
        # add user's info to profiles.json
        profiles[args.Username] = [args.Password, args.clearance_level]
        profiles_json = json.dumps(profiles)
        with open('session_data/profiles.json', 'w') as profiles:
            profiles.write(profiles_json)
    # if user does already exist
    else:
        print('Profile Exists \nSigning in...')
        # if user requested a higher clearance level than he previously had
        if args.clearance_level > profiles[args.Username][1]:
            print('User requested higher clearance level \nUser ' + args.Username + ' has level 0 clearance.')
        # otherwise -- if user wants to decrease clearance level -- update his profile
        elif args.clearance_level < profiles[args.Username][1]:
            if input('User has higher clearance: \nDo you wish to lower your clearance level to 0 [Enter Y]?') == 'Y':
                profiles[args.Username][1] = args.clearance_level
                profiles_json = json.dumps(profiles)
                with open('session_data/profiles.json', 'w') as profiles:
                    profiles.write(profiles_json)


if __name__ == '__main__':
    main()
