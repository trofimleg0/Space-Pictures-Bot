import os
import requests
from urllib.parse import urlsplit


def get_extension(url):
    splited_url = urlsplit(url)
    extension = os.path.splitext(splited_url.path)[1]

    return extension


def save_image(file_path, image_url, params=None):
    response = requests.get(image_url, params=params)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)
