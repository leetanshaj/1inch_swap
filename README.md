# 1inch_swap
1inch Swap API using PYTHON on BSC (Binance Smart Chain)

This bot can be used to swap from One Crypto Asset to Another using 1inch Exchange and BSC (Binance Smart Chain Route)<br>
Arbitrage Can be done using this api and further rules to set slippage and margin<br>
Instead of using Private Key, a local mainnet can be attached to Metamask for Transaction Approval which can lead to lesser fees <br>

Requirements
 1) pip install web3
 2) pip install --force-reinstall jsonschema==3.2.0

Paramters Explaination
  1) fromTokenAddress : Contract Address of Token to swap FROM 
  2) toTokenAddress   : Contract Address of Token to swap TO
  3) withdrawAccount  : Withdrawal Wallet Address 
  4) destReceiver     : Wallet address to receive the assets in ( Leave Blank if Withdraw Account is Same as Receiver )
  5) private_key      : Private key of the Withdraw Wallet
  6) slippage         : slippage % in int 
  7) gasLimit         : gas limit of to spend on transaction
  8) amount           : Amount of asset to Swap
  9) gasPrice         : Gas price to spend on transaction

Example Swap 1 BNB to USDT

1) fromTokenAddress = 0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE
2) toTokenAddress = 0x55d398326f99059ff775485246999027b3197955
3) withdrawAccount = "0xF15f243bb5xxxxxxxxxxxxxxxxxxxxxxxxxxx"
4) destReceiver = 0xF15f243bb5xxxxxxxxxxxxxxxxxxxxxxxxxxx
5) private_key = "18xxxxxxxb4325xxxxxxx8c9e4axxxxxxxc0b5c1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
6) slippage = 5
7) gasLimit = 10000000
8) amount = 1
9) gasPrice = 5000000000

For any queries email or raise a issue
