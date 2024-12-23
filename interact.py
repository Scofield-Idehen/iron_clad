import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os

load_dotenv()

MY_CONTRACT = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

def main():
    rpc = os.getenv("RPC_URL") 
    env = NetworkEnv(rpc=EthereumRPC(rpc))
    boa.set_env(env)


    anvil_key = os.getenv("ANVL_KEY")
    myaccount = Account.from_key(anvil_key)
    boa.env.add_account(myaccount, force_eoa=True)


    fav_partial = boa.load("dad.vy")

    fav_partial.set_bool(True)
    

    fac = fav_partial.get_bool()
    print(f"current bool value {fac}")




if __name__ == "__main__":
    main()