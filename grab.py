""" adds user's request (of certain type and amount) to his / her cart"""
import argparse
import json
import os
from PIL import Image
from system.catalog_generator import images
from system.system_clearance import auto_encode, predict


label1 = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Boot']
# labels allowed for clearance level 0
label0 = ['Top', 'Bottom', 'Shoe']


def main():
    # receive arguments from the command line
    parser = argparse.ArgumentParser()
    # argument 1: type (label) of clothing requested
    parser.add_argument('label', choices=(label1 + label0), help='request type of item')
    # argument 2: either --num or --all
    group = parser.add_mutually_exclusive_group(required=True)
    # argument 2.1: specify amount of clothes requested
    group.add_argument('-n', '--num', type=int, help='specify amount of items to grab of requested Label')
    # argument 2.2: request all clothes of requested type
    group.add_argument('-a', '--all', action='store_true', help='grab all items of requested Label')
    # argument 3: specify under what directory in cart to save request
    parser.add_argument('to_path', type=str, help='directory to store your items in')

    with open('session_data/surfer.json') as surfer_json:
        current_clr, current_user = json.load(surfer_json)

    # list of arguments passed
    args = parser.parse_args()

    # if user has no clearance level -- deny request
    if current_clr == 'No Clearance':
        print('Unauthorized: No Clearance')
    # if user with clearance level 0 requested type of clearance level 1 -- deny request
    elif current_clr == 0 and args.label in label1:
        print('Requested label unauthorized for User with your clearance level')
    else:
        # if user has clearance level 1, user can also search level 0 labels
        if current_clr == 1 and args.label in label0:
            current_clr = 0
        # if user has no cart -- create cart and add to_path directory
        if not os.path.exists(current_user):
            os.system('mkdir ' + current_user)
        os.system('mkdir ' + current_user + '/' + args.to_path)
        # if requested all -- search whole catalog
        if args.all:
            for i in range(len(images)):
                image = auto_encode(images[i], current_clr)
                label = predict(image)
                if label == args.label:
                    image = Image.fromarray(images[i])
                    image.save('./' + current_user + '/' + args.to_path + '/' + str(i) + '.png')
        # if requested specified number -- search through catalog until amount is found or no more items
        else:
            num = 0
            for i in range(len(images)):
                if num == args.num:
                    break
                image = auto_encode(images[i], current_clr)
                label = predict(image)
                if label == args.label:
                    num += 1
                    image = Image.fromarray(images[i])
                    image.save('./' + current_user + '/' + args.to_path + '/' + str(i) + '.png')
        # open requested order for user to review
        os.system('xdg-open ./' + current_user + '/' + args.to_path)


if __name__ == '__main__':
    main()
