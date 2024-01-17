import random
from config import *
from web3 import Web3
import time
from loguru import logger




class Tokenbridge:
    def __init__(self,source,dest,gasprice):
        if (source in source_chains) == False:
            logger.error(f"Неверный source chain. Укажите source chain из этого списка: {source_chains}")
        if (dest in dest_chains) == False:
            logger.error(f"Неверный dest chain. Укажите dest chain из этого списка: {dest_chains}")


        self.source_chain = source
        self.dest_chain = dest
        self.dest_chain_id = destchain_ids[dest]
        self.pool_id = pools[source]

        self.w3 = Web3(Web3.HTTPProvider(rpcs[source]))
        self.contract = self.w3.eth.contract(address=Web3.to_checksum_address(contracts[source]), abi=abis[source])
        self.gasprice = gasprice
        
        pass

    def bridge(self,amount,key):
        while (self.w3.eth.gas_price /10**9) > max_gas:
            print("высокий газ! пока спим")
            time.sleep(300)
        wallet_address = Web3.to_checksum_address(self.w3.eth.account.from_key(key).address)
        logger.info(f"аккаунт {wallet_address} запущен")
        nonce = self.w3.eth.get_transaction_count(wallet_address)
        bridge_fee = self.contract.functions.estimateFee(self.pool_id,self.dest_chain_id,Web3.to_wei(amount, 'ether')).call()
        print(f"bridge fee = {Web3.from_wei(bridge_fee,'ether')}")
        tx_params = {
            'from': wallet_address,
            'nonce': nonce,
            'value':  Web3.to_wei(amount, 'ether') + bridge_fee
        }

        if self.gasprice != -1:
            tx_params['gasPrice'] = Web3.to_wei(self.gasprice,'gwei')


        tx = self.contract.functions.transferETH(self.dest_chain_id,Web3.to_wei(amount, 'ether'), wallet_address).build_transaction(tx_params)
        signed_txn = self.w3.eth.account.sign_transaction(tx,key)
        print(tx)
        resp = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(resp)


def main():
    tokenbridge = Tokenbridge(source_chain,destination_chain,gasprice)
    for key in private_keys:
        amnt = random.uniform(amnt_FROM, amnt_TO)
        tokenbridge.bridge(amnt,key)
        t = random.randint(SLEEP_FROM, SLEEP_TO)
        print(f"спим {t} секунд")
        time.sleep(t)


main()
