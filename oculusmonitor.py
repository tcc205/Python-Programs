import requests
import json


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

response = requests.request("GET", url, headers=headers, data = payload)
resp = response.text
respDict = json.loads(resp)
lapremstock = 0
newyorkstock = 0
newyorkpremiumstock = 0
chicagostock = 0
virginiastock = 0
vaprem = 'Virginia_Premium'
for key, value in respDict.items():
  if key != vaprem:
    if value =

