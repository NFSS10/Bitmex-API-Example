# Bitmex API Example
Basic Bitmex operations needed to create a trading bot. For more information about the API: https://www.bitmex.com/app/apiOverview

## Installation
> pip install bitmex
>
> pip install bitmex-ws


## Usage
```python
import bitmex as Bitmex

leverage = 10
api_key = "YOUR API KEY HERE"
api_secret = "YOUR API SECRET HERE"

Bitmex.init(api_key, api_secret)

print("Setting the leverage to " + str(leverage) + "x")
Bitmex.setTradingLeverage(leverage)

orderData = Bitmex.buyMarket(50)
priceBought = orderData[0]['price']
print("Bought 50 contracts at the market price of "+ str(priceBought) + " $")
```
