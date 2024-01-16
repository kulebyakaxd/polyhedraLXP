import random
from config import *
from web3 import Web3
import time
from loguru import logger

w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.ninicoin.io"))
contract = w3.eth.contract(address=Web3.to_checksum_address(bsc_contractadr), abi=bsc_abi)


def bridge(amount,key):
    wallet_address = Web3.to_checksum_address(w3.eth.account.from_key(key).address)
    logger.info(f"аккаунт {wallet_address} запущен")
    nonce = w3.eth.get_transaction_count(wallet_address)
    bridge_fee = contract.functions.estimateFee(bsc_pool_id,transfer_chain_id,Web3.to_wei(amount, 'ether')).call()
    print(f"bridge fee = {Web3.from_wei(bridge_fee,'ether')}")
    tx_params = {
        'gasPrice': w3.eth.gas_price,
        'from': wallet_address,
        'nonce': nonce,
        'value':  Web3.to_wei(amount, 'ether') + bridge_fee
    }

    tx = contract.functions.transferETH(transfer_chain_id,Web3.to_wei(amount, 'ether'), wallet_address).build_transaction(tx_params)
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