"""
Basic Bitmex operations needed to create a trading bot.

How to use:
    1- Fill the API_KEY and API_SECRET with your keys.
    2- Call init to initalize the needed variables.
    Operations are now ready to be used !


To get realtime data use the WebSocket API,
    for handling orders, use the REST API

Follow the Bitmex documentation and add any method you need.
"""

import bitmex
from bitmex_websocket import BitMEXWebsocket


#WebSocket TEST: wss://testnet.bitmex.com/realtime.

#WebSocket LIVE: wss://www.bitmex.com/realtime


#region Variables
API_KEY = ""
API_SECRET = ""

bitmexWebSocket = None
bitmexClient = None
#endregion Variables



#Init the websocket and the client
def init(apiKey: str, apiSecret: str):
    """Setups the script initiating the WebSocket and Client"""
    global bitmexWebSocket, bitmexClient
    bitmexWebSocket = initBitmexWebSocket(apiKey, apiSecret)
    bitmexClient = initBitmexClient(apiKey, apiSecret)





#region Bitmex_WebSocket_API
"""
https://www.bitmex.com/app/wsAPI

Get real time data from Bitmex using a websocket, avoiding the limits of using the REST API
"""
def initBitmexWebSocket(apiKey: str, apiSecret: str):
    """Instantiate a connection"""
    ws = BitMEXWebsocket(endpoint="wss://testnet.bitmex.com/realtime", symbol="XBTUSD", api_key=apiKey, api_secret=apiSecret)
    ws.get_instrument()
    return ws



def getLastPrice():
    """Get last price of XBT"""
    global bitmexWebSocket
    return bitmexWebSocket.get_ticker()['last']

def recent_trades():
    """Get last price of XBT"""
    global bitmexWebSocket
    return bitmexWebSocket.recent_trades()
#endregion Bitmex_WebSocket_API





#region Bitmex_REST_API
"""
https://www.bitmex.com/api/explorer/


Handle orders using the Bitmex REST API
"""
def initBitmexClient(apiKey: str, apiSecret: str):
    """Get an instance of the client"""
    return bitmex.bitmex(test=True, api_key=apiKey, api_secret=apiSecret)



def setTradingLeverage(leverage: float):
    """Sets the account leverage"""
    global bitmexClient
    return bitmexClient.Position.Position_updateLeverage(symbol='XBTUSD', leverage=leverage).result()



def getOpenPositions():
    """Sets the account leverage"""
    global bitmexClient
    return bitmexClient.Position.Position_get().result()



def buyMarket(ammount: int):
    """Do a market buy with the ammount specified"""
    global bitmexClient
    return bitmexClient.Order.Order_new(symbol='XBTUSD', side="Buy", orderQty=ammount, ordType="Market").result()



def sellMarket(ammount: int):
    """Do a market sell with the ammount specified"""
    global bitmexClient
    return bitmexClient.Order.Order_new(symbol='XBTUSD', side="Sell", orderQty=ammount, ordType="Market").result()



def buyLimit(ammount: int, limitPrice: float):
    """Place a limit buy order with the ammount specified at the limit price specified"""
    global bitmexClient
    return bitmexClient.Order.Order_new(symbol='XBTUSD', side="Buy", orderQty=ammount, ordType="Limit", execInst="ParticipateDoNotInitiate", price=limitPrice).result()



def sellLimit(ammount: int, limitPrice: float):
    """Place a limit sell order with the ammount specified at the limit price specified"""
    global bitmexClient
    return bitmexClient.Order.Order_new(symbol='XBTUSD', side="Sell", orderQty=ammount, ordType="Limit", execInst="ParticipateDoNotInitiate", price=limitPrice).result()



def stopMarketSell(price: float):
    """Place a stop marketorder with the ammount specified at the price specified"""
    global bitmexClient
    return bitmexClient.Order.Order_new(symbol='XBTUSD', side="Sell", ordType="Stop", stopPx=price, execInst="Close").result()

def stopMarketBuy(price: float):
    """Place a stop marketorder with the ammount specified at the price specified"""
    global bitmexClient
    return bitmexClient.Order.Order_new(symbol='XBTUSD', side="Buy", ordType="Stop", stopPx=price, execInst="Close").result()



def closeOrder():
    """Close the opened order at market price"""
    global bitmexClient
    return bitmexClient.Order.Order_closePosition(symbol='XBTUSD').result()


def cancelAll():
    """Cancels all pending orders"""
    global bitmexClient
    return bitmexClient.Order.Order_cancelAll(symbol='XBTUSD').result()
#endregion Bitmex_REST_API





__author__ = 'Nuno Silva aka NFSS10'
#http://nfss10.com/