import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Username', type=str)
    parser.add_argument('Password', type=str)
    parser.add_argument('clearance_level', type=int, choices=[0, 1])

    with open('session_data/profiles.json') as profiles_json:
        profiles = json.load(profiles_json)

    args = parser.parse_args()

    if args.Username not in profiles:
        profiles[args.Username] = [args.Password, args.clearance_level]
        profiles_json = json.dumps(profiles)
        with open('session_data/profiles.json', 'w') as profiles:
            profiles.write(profiles_json)
    else:
        print('Profile Exists \nSigning in...')
        if args.clearance_level > profiles[args.Username][1]:
            print('User requested higher clearance level \nUser ' + args.Username + ' has level 0 clearance.')
        elif args.clearance_level < profiles[args.Username][1]:
            if input('User has higher clearance: \nDo you wish to lower your clearance level to 0 [Enter Y]?') == 'Y':
                profiles[args.Username][1] = args.clearance_level
                profiles_json = json.dumps(profiles)
                with open('session_data/profiles.json', 'w') as profiles:
                    profiles.write(profiles_json)


if __name__ == '__main__':
    main()
