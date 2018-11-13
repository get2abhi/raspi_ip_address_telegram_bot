import logging.handlers, telegram
import netifaces as ni

LOG_FILENAME = '/home/pi/dev/myipaddress.log'
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=102400, backupCount=5)
my_logger.addHandler(handler)

token = 'TOKEN'

ip = 'Unknown'
try:
	addrs = ni.ifaddresses('wlan0')
	ip = addrs[ni.AF_INET][0]['addr']
except Exception as e:
	my_logger.error(str(e))
	ip = 'I lost conneyction to Wifi', e

bot = telegram.Bot(token=token)
chat_id = bot.get_updates()[-1].message.chat_id
bot.send_message(chat_id=chat_id, text="Hey Dude. My new IP Address is " + ip)
