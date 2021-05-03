from web3 import Web3
import requests

def intToDecimal(qty, decimal):
  return int(qty * int("".join(["1"] + ["0"]*decimal)))
def decimalToInt(price, decimal):
  return price/ int("".join((["1"]+ ["0"]*decimal)))
def get_api_call_data(url):
	try: call_data = requests.get(url)
	except Exception as e:
		print(e)
		return get_api_call_data(url)
	try:
		api_data = call_data.json()
    	return api_data
	except Exception as e: 
		print(call_data.text) 


fromTokenAddress = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
toTokenAddress = "0x55d398326f99059ff775485246999027b3197955"
withdrawAccount = "0xF15f243bb5xxxxxxxxxxxxxxxxxxxxxxxxxxx"
destReceiver = "0xF15f243bb5xxxxxxxxxxxxxxxxxxxxxxxxxxx"
private_key = '18xxxxxxxb4325xxxxxxx8c9e4axxxxxxxc0b5c1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
slippage = 5
gasLimit = 10000000
amount = intToDecimal(1) 
gasPrice = 5000000000
ChainUrl = "https://bsc-dataseed1.binance.org:443"
_1inchurl = f'https://api.1inch.exchange/v3.0/56/swap?fromTokenAddress={fromTokenAddress}&toTokenAddress={toTokenAddress}&amount={amount}&fromAddress={withdrawAccount}&destReceiver={destReceiver}&slippage={slippage}&gasPrice={gasPrice}&gasLimit={gasLimit}'


json_data = get_api_call_data()
web3 = Web3(Web3.HTTPProvider(ChainUrl))
nonce = web3.eth.getTransactionCount(withdrawAccount)
tx = json_data['tx']
tx['nonce'] = nonce
tx['to'] = Web3.toChecksumAddress(tx['to'])
tx['gasPrice'] = int(tx['gasPrice'])
tx['value'] = int(tx['value'])
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
# to check transaction 
# https://bscscan.com/tx/<tx_hash> #replace <tx_hash> with value of tx_hash
