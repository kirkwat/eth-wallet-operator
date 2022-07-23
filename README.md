# Ethereum Wallet Operator

## Functionality
This application connects a user to the Ethereum blockchain where they can view the ETH balance of any wallet address and send ETH transactions using their own wallet.

## How to Use
To use this application, the user will need to fill the config.json input file with a HTTPS RPC URL and the private key of their Ethereum wallet. The RPC URL will allow the application to connect to the Ethereum network. The URL can be from either a local node or key from a provider such as Alchemy or Infura. Here's an example on Youtube of how to get a free RPC from Alchemy: https://www.youtube.com/watch?v=tfggWxfG9o0&t

If interested in testing the application on a simulator blockchain, download Ganache here: https://trufflesuite.com/ganache/index.html. Ganache allows developers to test the functionality of the Ethereum blockchain without risking money and security. After installation, click Quick Start to generate a testing environment. Copy the RPC Server URL and paste it into config.json. The testing environment also includes wallets with accessible private keys that can be used in the application. Once the config.json is saved with a working RPC and private key, install the required dependencies by entering the following command in the terminal:
### `pip install -r requirements.txt`

Once the config.json is saved with a working RPC and private key, enter the following command to start the application: 
### `python app.py`

The application will connect to the network and authenticate the user's wallet. If unsuccessful, the application will give a warning and shut down. Otherwise, a menu shall appear allowing the user to send Ethereum or view wallet balances.
