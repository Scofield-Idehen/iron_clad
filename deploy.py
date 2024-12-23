import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os

load_dotenv()


def main():
    rpc = os.getenv("RPC_URL") 
    env = NetworkEnv(rpc=EthereumRPC(rpc))
    boa.set_env(env)


    anvil_key = os.getenv("ANVL_KEY")
    myaccount = Account.from_key(anvil_key)
    boa.env.add_account(myaccount, force_eoa=True)

    fav_contract = boa.load("dad.vy")

    starting_fav_number = fav_contract.get_bool()
    print(f"Starting fav number: {starting_fav_number}")




if __name__ == "__main__":
    main()
