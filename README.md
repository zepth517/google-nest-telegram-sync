
# Google Nest camera clips - Telegram channel sync

This project is a fork of [@TamiMa's repository](https://github.com/TamirMa/google-nest-telegram-sync), implementing support for python 3.13, fixing some scheduling bugs, as well as exposing the timezone as a configuration option.

## Features

- Get list of **Google Home devices through HomeGraph**
- Retrieve recent **Google Nest events**
- Download **full-quality Google Nest video clips**
- Send those clips to a Telegram channel


## Usage:

* Install the required dependencies:
  ```bash
    pip install -r requirements.txt
  ```

* Get a Google "Master Token", using the [ha-google-home_get-token](https://hub.docker.com/r/breph/ha-google-home_get-token) docker image.

  ```bash
    docker run --rm -it breph/ha-google-home_get-token
  ```

* Create a .env file with the following contents:

  ```dotenv
  GOOGLE_MASTER_TOKEN="aas_..."
  GOOGLE_USERNAME="youremailaddress@gmail.com"
  TELEGRAM_BOT_TOKEN="token..."
  TELEGRAM_CHANNEL_ID="-100..."
  TIMEZONE="US/Central"
  ```

  Use [@username_to_id_bot](https://t.me/username_to_id_bot) to get the channel id of a private channel.
  
  All available timezones can be found [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568)
  

* Then run:

  ```bash
    python3 main.py
  ```

## Credits:

- [original repository](https://github.com/TamirMa/google-nest-telegram-sync) from which this project is forked
- [glocaltokens](https://github.com/leikoilja/glocaltokens) for the Google Home Graph API
- [ha-google-home_get-token](https://hub.docker.com/r/breph/ha-google-home_get-token) for the Google Master Token retrieval process
- [python-telegram-bot](https://python-telegram-bot.org/) for the Telegram API
