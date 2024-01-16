import json


# mantle = 20 combo = 27
transfer_chain_id = 27

max_gas = 4

SLEEP_FROM = 300
SLEEP_TO = 400

amnt_FROM = 0.0001
amnt_TO = 0.0002




bsc_contractadr = '0x51187757342914E7d94FFFD95cCCa4f440FE0E06'
linea_contractadr = '0x366C1B89aA0783d0886B9EF817d10c8729783dCb'

bsc_pool_id = 10
linea_pool_id = 1

with open('abis/lineaABI.json') as f:
    linea_abi = json.load(f)

with open('abis/bscABI.json') as f:
    bsc_abi = json.load(f)


with open("accounts.txt") as f:
    private_keys = [r.strip() for r in f.readlines()]
