import requests
import json
import time
from dhooks import Webhook, Embed
import math


def sendHooks(value, type, link):
  stock = (value / 25)
  amount = math.floor(stock)
  hook = Webhook('https://discordapp.com/api/webhooks/704560730749272064/jFr8w0aP5gxOZL0ImAJb53F94xWAxfezRk3cyD3Y9E0msBPSFwQSv_PpqR-g4XV3pupx')

  embed = Embed(
    #description='Oculus proxies restocked ' + str(numpacks) + " packs of " + type,
    color=0x5CDBF0,
    timestamp='now'  # sets the timestamp to current time
  )

  image1 = 'https://pbs.twimg.com/profile_images/1000760087546392576/UJBqUta8.jpg'
  image2 = 'https://pbs.twimg.com/profile_images/1000760087546392576/UJBqUta8.jpg'

  embed.set_author(name='Oculus Proxies Restock\n-->CLICK ME<--', icon_url=image1, url=link)
  embed.add_field(name='Type', value=type)
  embed.add_field(name='Amount\n(sold in 25x)', value=str(amount))
  embed.set_footer(text='Made by @thecanoechief', icon_url=image1)

  embed.set_thumbnail(image1)
  embed.set_image(image2)

  hook.send("@everyone", embed=embed)
  stockRequest()

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
  nyPremium(respDict)
  laPremium(respDict)
  nyRegular(respDict)
  chiRegular(respDict)
  vaRegular(respDict)

def nyPremium(respDict):
  nypremstock = 1
  nyprem = 'NewYork_Premium'
  running = True
  while running == True:
    for key, value in respDict.items():
      if key == nyprem:
        if value > nypremstock:
          type = 'NY Premium'
          link = 'https://oculusproxies.com/premium_pricing'
          sendHooks(value, type, link)
          nypremstock = value
          running = True
          break
        else:
          print("no restock found")
          time.sleep(4)
          nypremstock = value
          break

def laPremium(respDict):
  lapremstock = 0
  laprem = 'Los_Angeles_Premium'
  running = True
  while running == True:
    for key, value in respDict.items():
      if key == laprem:
        if value > lapremstock:
          type = 'LA Premium'
          link = 'https://oculusproxies.com/premium_pricing'
          sendHooks(value, type, link)
          lapremstock = value
          running = True
          break
        else:
          print("no restock found")
          lapremstock = value
          time.sleep(4)
          stockRequest()
          break

def nyRegular(respDict):
  nyRegstock = 0
  nyreg = 'NewYork'
  running = True
  while running == True:
    for key, value in respDict.items():
      if key == nyreg:
        if value > nyRegstock:
          type = 'NY Regular'
          link = 'https://oculusproxies.com/pricing'
          sendHooks(value, type, link)
          nyRegstock = value
          running = True
          break
        else:
          print("no restock found")
          nyRegstock = value
          time.sleep(4)
          stockRequest()
          break

def chiRegular(respDict):
  chiRegstock = 0
  chireg = 'Chicago'
  running = True
  while running == True:
    for key, value in respDict.items():
      if key == chireg:
        if value > chiRegstock:
          type = 'Chicago Regular'
          link = 'https://oculusproxies.com/pricing'
          sendHooks(value, type, link)
          chiRegstock = value
          running = True
          stockRequest()
          break
        else:
          print("no restock found")
          chiRegstock = value
          time.sleep(4)
          break

def vaRegular(respDict):
  vaRegstock = 0
  vareg = 'Virginia'
  running = True
  while running == True:
    for key, value in respDict.items():
      if key == vareg:
        if value > vaRegstock:
          type = 'Virginia Regular'
          link = 'https://oculusproxies.com/pricing'
          sendHooks(value, type, link)
          vaRegstock = value
          running = True
          break
        else:
          print("no restock found")
          vaRegstock = value
          time.sleep(4)
          stockRequest()
          break

#value = 76
#link = 'https://oculusproxies.com/premium_pricing'
#type = 'NY Premium'
#sendHooks(value, type, link)

stockRequest()

