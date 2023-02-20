import os
import requests
import additional_functions
from pathlib import Path
from dotenv import load_dotenv


def get_epic_images_data(nasa_token, epic_url):
    params = {'api_key': nasa_token}

    response = requests.get(epic_url, params=params)
    response.raise_for_status()

    return response.json()


if __name__ == '__main__':
    load_dotenv()

    image_path = os.environ['IMAGE_PATH']
    Path(image_path).mkdir(parents=True, exist_ok=True)

    nasa_token = os.environ['NASA_TOKEN']
    epic_date = os.environ['EPIC_DATE']
    epic_url = f'https://api.nasa.gov/EPIC/api/natural/date/{epic_date}'
    year, month, day = epic_date.split()[0].split('-')

    try:
        epic_images_data = get_epic_images_data(nasa_token, epic_url)
        for image_num, epic_image_data in enumerate(epic_images_data, 1):
            image_name = epic_image_data['image']
            epic_url = f'https://api.nasa.gov/EPIC/archive/natural/' \
                       f'{year}/{month}/{day}/png/{image_name}.png'
            params = {'api_key': nasa_token}

            additional_functions.save_image(
                f'{image_path}EPIC_{image_num}.png', epic_url, params)
    except requests.exceptions.HTTPError:
        print('Error 404. Page Not Found')
