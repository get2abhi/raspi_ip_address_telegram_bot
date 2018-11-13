# raspi_ip_address_telegram_bot
A raspberry pi telegram bot to send you the ip address of raspi without the need of monitor
sdasd

## Generating Telegram Bot Token

1. First you need to install and setup telegram on your mobile phone or laptop from https://telegram.org/
2. Next search for the BotFather bot on telegram by searching `@BotFather` or by visiting https://telegram.me/BotFather 
3. Send `/newbot <your new bot name>` command to BotFather and it will create a new bot by that name
4. Send `/token` command to get a auth token for this bot

## Using Telegram Bot Token

1. Replace token in line 10 of myaddress.py with the token received from step 4 above

## Running the bot

1. Start chatting with your new bot by sending some message.
2. Make sure the path to the log file exists in line 4 of myipaddress.py
3. Install telegram library for python

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pip install python-telegram-bot`

3. Just run the bot with `python myipaddress.py` and you should be getting the ip address of the raspi<br><br>
`Hey Dude. My new IP Address is 192.168.1.111`

## Putting the script on boot

1. Open Crontab using `crontab -e`
2. Add an entry at the bottom like this (Make sure the script exists on the path)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`@reboot sleep 60 && python dev/scripts/myipaddress.py &`

3. Send a test message to the bot everytime when you need the ip address before boot.
