import argparse
import json
import os
from PIL import Image
from system.catalog_generator import images
from system.system_clearance import auto_encode, predict


label1 = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Boot']
label0 = ['Top', 'Bottom', 'Shoe']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('label', choices=(label1 + label0), help='request type of item')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-n', '--num', type=int, help='specify amount of items to grab of requested Label')
    group.add_argument('-a', '--all', action='store_true', help='grab all items of requested Label')
    parser.add_argument('to_path', type=str, help='directory to store your items in')

    with open('session_data/surfer.json') as surfer_json:
        current_clearance_level, current_user = json.load(surfer_json)

    args = parser.parse_args()

    if current_clearance_level == 'No Clearance':
        print('Unauthorized: No Clearance')
    elif current_clearance_level == 0 and args.label in label1:
        print('Requested label unauthorized for User with your clearance level')
    else:
        # if user has clearance level 1, user can also search level 0 labels
        if current_clearance_level == 1 and args.label in label0:
            current_clearance_level = 0
        if not os.path.exists(current_user):
            os.system('mkdir ' + current_user)
        os.system('mkdir ' + current_user + '/' + args.to_path)
        if args.all:
            for i in range(len(images)):
                image = auto_encode(images[i], current_clearance_level)
                label = predict(image)
                if label == args.label:
                    image = Image.fromarray(images[i])
                    image.save('./' + current_user + '/' + args.to_path + '/' + str(i) + '.png')
        else:
            num = 0
            for i in range(len(images)):
                if num == args.num:
                    break
                image = auto_encode(images[i], current_clearance_level)
                label = predict(image)
                if label == args.label:
                    num += 1
                    image = Image.fromarray(images[i])
                    image.save('./' + current_user + '/' + args.to_path + '/' + str(i) + '.png')
        os.system('xdg-open ./' + current_user + '/' + args.to_path)


if __name__ == '__main__':
    main()
