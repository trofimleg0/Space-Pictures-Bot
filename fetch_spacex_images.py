import os
import argparse
import requests
import additional_functions
from pathlib import Path
from dotenv import load_dotenv


def get_args():
    parser = argparse.ArgumentParser(
        description='Download spaceX launch pictures')
    parser.add_argument('launch_id',
                        nargs='?',
                        default='latest',
                        help='Please select the launch ID')

    return parser.parse_args().launch_id


def get_spacex_launch_urls(launch_url):
    response = requests.get(launch_url)
    response.raise_for_status()

    return response.json()['links']['flickr']['original']


if __name__ == '__main__':
    load_dotenv()

    image_path = os.environ['IMAGE_PATH']
    Path(image_path).mkdir(parents=True, exist_ok=True)

    launch_id = get_args()
    launch_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    try:
        spacex_launch_urls = get_spacex_launch_urls(launch_url)
        for image_num, spacex_launch_url in enumerate(spacex_launch_urls, 1):
            extension = additional_functions.get_extension(spacex_launch_url)
            image_name = f'spaceX_{image_num}'
            additional_functions.save_image(
                f'{image_path}{image_name}{extension}', spacex_launch_url)
    except requests.exceptions.HTTPError:
        print('Error 404. Page Not Found')
