import sys
from os import path, pardir
sys.path.append(path.join(path.dirname(path.abspath(__file__)), pardir))
from cubepay.client import CubePayClient
from example._config import CLIENT_ID,CLIENT_SECRET,URL

client = CubePayClient(CLIENT_ID,CLIENT_SECRET,URL)

coins = client.get_coin()
print(coins)
