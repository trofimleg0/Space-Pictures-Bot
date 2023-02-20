import os
import time
import telegram
from random import shuffle
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    image_path = os.environ['IMAGE_PATH']
    bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])
    chat_id = os.environ['CHAT_ID']

    image_names = os.listdir(image_path)

    while True:
        for image_name in image_names:
            with open(f'{image_path}{image_name}', 'rb') as photo:
                bot.send_photo(chat_id, photo=photo)
            time.sleep(int(os.environ['DELAY']))
        shuffle(image_names)
