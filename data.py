import json

source_chains = ['bsc','linea']
dest_chains = ['combo','mantle']


rpcs = {
    "bsc": "https://rpc.ankr.com/bsc",
    "linea": "https://rpc.linea.build"
}

destchain_ids = {
    'mantle': 20,
    'combo' : 27
}


contracts = {
    "bsc": "0x51187757342914E7d94FFFD95cCCa4f440FE0E06",
    "linea": "0x366C1B89aA0783d0886B9EF817d10c8729783dCb"
}

pools = {
    "bsc" : 10,
    "linea": 1
}


with open('abis/lineaABI.json') as f:
    linea_abi = json.load(f)

with open('abis/bscABI.json') as f:
    bsc_abi = json.load(f)

abis = {
    "bsc": bsc_abi,
    "linea": linea_abi
}

with open("accounts.txt") as f:
    private_keys = [r.strip() for r in f.readlines()]