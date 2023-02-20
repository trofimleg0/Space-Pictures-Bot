# Space-pictures

Publishes images of NASA and SpaceX obtained using the API in the telegram

## How to install ##

Python should be already installed.  

Use `pip`(or `pip3` for Python3) to install dependencies:

```commandline
pip install -r requirements.txt
```

Recommended using [virtualenv/venv](https://docs.python.org/3/library/venv.html)

## Launch ##

1) [Generate](https://api.nasa.gov) NASA API Key
2) [Register](https://web.telegram.org/k/) and [Create](https://telegram.me/BotFather) the telegram bot to get the Token([How](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0))
3) Create the Telegram Public Channel and add the bot as administrator
4) Add to `.env` file:
    - `NASA_TOKEN` - Your generated NASA token
    - `IMAGE_PATH` - The path where you will get images
    - `APOD_START_DATE` - The start date for the APOD image request
    - `APOD_END_DATE` - The end date for the APOD image request
    - `EPIC_DATE` - The date for the EPIC image request
    - `TELEGRAM_TOKEN` - Your generated Telegram token
    - `CHAT_ID` - Your Channel ID in Telegram
    - `DELAY` - The interval of publication of images (in seconds)

### Download images of space: ###

Run `python fetch_spacex_images.py` with the optional ID parameter to get photos from a specific launch  
If the ID is not set, downloads photos from the latest launch

```commandline
python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```

Run `fetch_apod_images.py` to get NASA Astronomy Pictures of the Day

```commandline
python fetch_apod_images.py
```

Run `fetch_epic_images.py` to get NASA EPIC photos

```commandline
python fetch_epic_images.py
```

### Telegram bot: ###

Run `telegram_bot.py` to publish photos from `IMAGE_PATH` with the `DELAY`

```commandline
python telegram_bot.py
```

Run `post_one_image.py` with the optional "image name" parameter to publish one photo from `IMAGE_PATH`  
If the parameter is not set a random photo will be published from `IMAGE_PATH`

```commandline
python post_one_image.py EPIC_1.png
```

