import requests
import json
import time
from discord_webhooks import DiscordWebhooks


def sendHooks():

  # Webhook URL for your Discord channel.
  WEBHOOK_URL = 'https://discordapp.com/api/webhooks/586388906400808970/-ejCZGhvPk943qo9iq3vNLjWHGIJz69gFlDHu54B2LABcH28EvK3oZ9mALLh-L-a1i4_'

  webhook = DiscordWebhooks(WEBHOOK_URL)

  webhook.set_content(content='The best cat ever is...', title='Montezuma!', description='Seriously!', \
                      url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')

  # Attaches an image
  webhook.set_image(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

  # Attaches a thumbnail
  webhook.set_thumbnail(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

  # Attaches an author
  webhook.set_author(name='James Ives', url='https://jamesiv.es',
                     icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

  # Attaches a footer
  webhook.set_footer(text='Footer', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

  # Appends a field
  webhook.add_field(name='Field', value='Value!')

  webhook.send()



sendHooks()

def stockRequest():
  url = "https://oculusproxies.com/proxyconfig/getProxyStockCount"

  payload = {}
  headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9'
  }

  proxies = {
   "http" : "http://Ghd897!a113:TDv7iMyW@51.81.97.119:33128",
   "https": "http://Ghd897!a113:TDv7iMyW@51.81.97.119:33128",
  }

  response = requests.request("GET", url, headers=headers, data = payload, proxies=proxies)
  resp = response.text
  respDict = json.loads(resp)

def nyPremium():
  nypremstock = 1
  nyprem = 'NewYork_Premium'
  running = True
  while running == True:
    for key, value in respDict.items():
      if key == nyprem:
        if value != nypremstock:
          sendHooks()
          print("hi")
          nypremstock = value
          running = True
          break
        else:
          print("no restock found")
          time.sleep(1.5)
          break



