import os
import requests
import additional_functions
from pathlib import Path
from dotenv import load_dotenv


def get_apod_nasa_urls(nasa_token, start_date, end_date):
    params = {
        'api_key': nasa_token,
        'start_date': start_date,
        'end_date': end_date
    }

    response = requests.get('https://api.nasa.gov/planetary/apod',
                            params=params)
    response.raise_for_status()

    return [
        row['hdurl'] for row in response.json() if row['media_type'] == 'image'
    ]


if __name__ == '__main__':
    load_dotenv()

    image_path = os.environ['IMAGE_PATH']
    Path(image_path).mkdir(parents=True, exist_ok=True)

    nasa_token = os.environ['NASA_TOKEN']
    start_date = os.environ['APOD_START_DATE']
    end_date = os.environ['APOD_END_DATE']

    try:
        apod_nasa_urls = get_apod_nasa_urls(nasa_token, start_date, end_date)
        for image_num, apod_nasa_url in enumerate(apod_nasa_urls, 1):
            extension = additional_functions.get_extension(apod_nasa_url)
            image_name = f'NASA_APOD_{image_num}'
            additional_functions.save_image(
                f'{image_path}{image_name}{extension}', apod_nasa_url)
    except requests.exceptions.HTTPError:
        print('Error 404. Page Not Found')
