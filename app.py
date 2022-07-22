import json
import os
import time
from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware

#clear terminal
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clear()
#read file
try:
    config=json.load(open('config.json'))
except Exception as e:
    print("\033[31m... Unable to read config.json\033[0m")
    print("Closing in 5 seconds ...")
    time.sleep(5)
    exit()
# connect to blockchain
web3 = Web3(Web3.HTTPProvider(config['rpc']))
if bool(web3.isConnected()):
    print("\033[32m... Successfully connected to blockchain\033[0m")
else:
    print("\033[31m... Cannot connect to the blockchain. Please use working RPC\033[0m")
    print("Closing in 5 seconds ...")
    time.sleep(5)
    exit()
#connect to wallet
try:
    account: LocalAccount = Account.from_key(config['private_key'])
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    print("\033[32m... Successfully connected to wallet\033[0m")
except:
    print("\033[31m... Cannot authenticate wallet. Please use correct private key\033[0m")
    print("Closing in 5 seconds ...")
    time.sleep(5)
    exit()
#menu
option = '1'
while option != '0':
    #display menu
    print("Welcome to Kirk's Ethereum Wallet Operator!\n")
    print("Menu:")
    print("  \033[34m[1]\033[0m View ETH Balance")
    print("  \033[34m[2]\033[0m Send ETH")
    print("  \033[36m[0]\033[0m Close")
    option = input('Please input command: ')
    #view ethereum balance
    if option == '1':
        clear()
        #view balance menu
        retry='1'
        while retry=='1':
            view_option = input("Do you want to view your wallet's balance \033[32m(1)\033[0m or view the balance of another wallet \033[32m(2)\033[0m ? ")
            #view user balance
            if view_option=='1':
                print("Balance: "+"{:.2f}".format(web3.fromWei(web3.eth.getBalance(account.address), "ether"))+" ETH\n")
                retry='0'
            #view other address
            elif view_option=='2':
                #get address
                input_check=1
                while input_check:
                    search_addy = input("Please input the address to be searched: ")
                    #check if address is valid
                    if web3.isAddress(search_addy):
                        print("Balance: "+"{:.2f}".format(web3.fromWei(web3.eth.getBalance(search_addy), "ether"))+" ETH\n")
                        input_check=0
                    #invalid address
                    else:
                        print("\033[31mPlease input a valid address.\033[0m")
                retry='0'
            #invalid input
            else:
                print("\033[31mPlease input a valid option.\033[0m")
                retry='1'
    #send ethereum transaction 
    elif option == '2':
        clear()
        #get transaction input
        #get address
        input_check=1
        while input_check:
            recipient = input("Please input the recipient address: ")
            #check if address is valid
            if web3.isAddress(recipient):
                input_check=0
            #invalid address
            else:
                print("\033[31mPlease input a valid address.\033[0m")
        #get eth amount
        input_check=1
        while input_check:
            eth_value = input("Please input the amount of ETH that you would like to send: ")
            #check if input is valid
            try:
                val=float(eth_value)
                if val>0:
                    input_check=0
                else:
                    print("\033[31mPlease input a valid number.\033[0m")
            except ValueError:
                print("\033[31mPlease input a valid number.\033[0m")
        #get gas amount
        input_check=1
        while input_check:
            gas_value = input("Please input how much gwei you would like to send for this transaction: ")
            #check if input is valid
            try:
                val=float(gas_value)
                if val>0:
                    input_check=0
                else:
                    print("\033[31mPlease input a valid number.\033[0m")
            except ValueError:
                print("\033[31mPlease input a valid number.\033[0m")
        #create transaction
        txn = {
            'nonce': web3.eth.getTransactionCount(account.address),
            'to': recipient,
            'value': web3.toWei(eth_value, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei(gas_value, 'gwei'),
        }
        #sign and send transaction
        print("\nSending transaction of "+"{:.2f}".format(float(eth_value))+" ETH to "+recipient)
        try:
            txn_hash = web3.eth.sendRawTransaction(web3.eth.account.signTransaction(txn, config['private_key']).rawTransaction)
            #display hash
            print("Transaction hash: "+web3.toHex(txn_hash)+"\n")
        except Exception as e:
            print("\033[31mError sending transaction. Please make sure you have enough funds.\033[0m")
    #end program
    elif option == '0':
        print("Thank you for using this program. Goodbye!")
        time.sleep(2)
        break
    #invalid input
    else:
        print("\n\033[31mPlease input a valid option.\033[0m")
    #return to menu    
    input("Press Enter to continue...\n")
    clear()