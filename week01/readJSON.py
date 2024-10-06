# read a URL from the internet in JSON
# Author: Joanna Kelly

import requests

url ="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print(data["bpi"]["EUR"]["rate_float"])



