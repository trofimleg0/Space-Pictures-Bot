import os
import argparse
import telegram
from random import choice
from dotenv import load_dotenv


def get_args(image_names):
    parser = argparse.ArgumentParser(description='Publish one image')
    parser.add_argument('image_name',
                        nargs='?',
                        default=choice(image_names),
                        help='Please select the one name of image')

    return parser.parse_args().image_name


if __name__ == '__main__':
    load_dotenv()

    image_path = os.environ['IMAGE_PATH']
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    chat_id = os.environ['CHAT_ID']

    image_name = get_args(os.listdir(image_path))

    with open(f'{image_path}{image_name}', 'rb') as photo:
        bot.send_photo(chat_id, photo=photo)
