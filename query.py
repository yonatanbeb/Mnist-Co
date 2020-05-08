""" returns the type (according to current users' clearance level) of image in catalog """
import argparse
import json
from system.catalog_generator import images
from system.system_clearance import auto_encode, predict


def main():
    # receive arguments from the command line
    parser = argparse.ArgumentParser()
    # argument 1: number of catalog image to query
    parser.add_argument('item_code', type=int, help='catalog code of query item => check out catalog by typing: browse')

    # get current users' clearance level
    with open('session_data/surfer.json') as surfer_json:
        current_clr, _ = json.load(surfer_json)

    # list of arguments passed
    args = parser.parse_args()

    # auto encode image with clearance level
    image = auto_encode(images[args.item_code], current_clr)
    # predict contents of image
    label = predict(image)
    # display query answer
    print(label)


if __name__ == '__main__':
    main()
