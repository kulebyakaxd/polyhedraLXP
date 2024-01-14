import random
from web3 import Web3
from config import *
import time
from loguru import logger

w3 = Web3(Web3.HTTPProvider("https://1rpc.io/linea"))
contract = w3.eth.contract(address=Web3.to_checksum_address("0x366C1B89aA0783d0886B9EF817d10c8729783dCb"), abi=abi)


def bridge(amount,key):
    address = Web3.to_checksum_address(w3.eth.account.from_key(key).address)
    logger.info(f"аккаунт {address} запущен")
    nonce = w3.eth.get_transaction_count(address)
    bridge_fee = contract.functions.estimateFee(1,transfer_chain_id,Web3.to_wei(amount, 'ether')).call()
    print(f"bridge fee = {Web3.from_wei(bridge_fee,'ether')}")
    tx_params = {
        'gasPrice': w3.eth.gas_price,
        'from': address,
        'nonce': nonce,
        'value':  Web3.to_wei(amount, 'ether') + bridge_fee
    }

    tx = contract.functions.transferETH(transfer_chain_id,Web3.to_wei(amount, 'ether'), address).build_transaction(tx_params)
    signed_txn = w3.eth.account.sign_transaction(tx,key)
    resp = w3.eth.send_raw_transaction(signed_txn.rawTransaction) 


def main():
    for key in private_keys:
        amnt = random.uniform(amnt_FROM, amnt_TO)
        while (w3.eth.gas_price /10**9) > max_gas:
            print("высокий газ! пока спим")
            time.sleep(300)
        bridge(amnt,key)
        t = random.randint(SLEEP_FROM, SLEEP_TO)
        print(f"спим {t} секунд")
        time.sleep(t)


main()