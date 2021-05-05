from websocket import create_connection
import re
ws = create_connection("wss://stream.binance.com/stream")
pair = 'bnbusdt' #BNB-USDT
ws.send('{"method":"SUBSCRIBE","params":["'+pair+'@aggTrade"],"id":1}')
ws.recv()
oldPrice = float(re.findall('"p":"([\d.]+)',ws.recv())[0])
print(oldPrice)
while(True):
	price = float(re.findall('"p":"([\d.]+)',ws.recv())[0])
	if (100 * (price-oldPrice)/oldPrice > 0.05):
		print(price)
	if price>oldPrice:
		oldPrice = price
		print(price)
