import argparse
import json
from system.catalog_generator import images
from system.system_clearance import auto_encode, predict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('item_code', type=int, help='catalog code of query item => check out catalog by typing: browse')

    with open('session_data/surfer.json') as surfer_json:
        current_clearance_level, _ = json.load(surfer_json)

    args = parser.parse_args()

    image = auto_encode(images[args.item_code], current_clearance_level)
    label = predict(image)
    print(label)


if __name__ == '__main__':
    main()
