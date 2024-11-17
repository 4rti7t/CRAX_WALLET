import sys
import requests
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from eth_account import Account
import time

# Replace with your actual Etherscan API key
ETHERSCAN_API_KEY = '7XX8YH287DCVYQXX7IMMWEIFGMXV1RQ5T5'

ascii_art = """
▄████▄   ██▀███   ▄▄▄      ▒██   ██▒       █     █░ ▄▄▄       ██▓     ██▓    ▓█████▄▄▄█████▓   
▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒▒ █ █ ▒░      ▓█░ █ ░█░▒████▄    ▓██▒    ▓██▒    ▓█   ▀▓  ██▒ ▓▒   
▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ░░  █   ░      ▒█░ █ ░█ ▒██  ▀█▄  ▒██░    ▒██░    ▒███  ▒ ▓██░ ▒░   
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██  ░ █ █ ▒       ░█░ █ ░█ ░██▄▄▄▄██ ▒██░    ▒██░    ▒▓█  ▄░ ▓██▓ ░    
▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ▒██▒      ░░██▒██▓  ▓█   ▓██▒░██████▒░██████▒░▒████▒ ▒██▒ ░    
░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▒ ░ ░▓ ░      ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░ ▒ ░░      
  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░░   ░▒ ░        ▒ ░ ░    ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░   ░       
░          ░░   ░   ░   ▒    ░    ░          ░   ░    ░   ▒     ░ ░     ░ ░      ░    ░         
░ ░         ░           ░  ░ ░    ░            ░          ░  ░    ░  ░   ░  ░   ░  ░           
░                                                                                                
"""
print(ascii_art)

def is_valid_mnemonic(mnemonic):
    try:
        return Mnemonic("english").check(mnemonic)
    except Exception as e:
        return False

def get_bitcoin_address(mnemonic):
    seed = Mnemonic("english").to_seed(mnemonic)
    hd_key = HDKey.from_seed(seed, network='bitcoin')
    return hd_key.address()

def get_ethereum_address(mnemonic):
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(mnemonic)
    return account.address

def get_bitcoin_balance(address):
    url = f"https://blockchain.info/q/addressbalance/{address}"
    try:
        response = requests.get(url)
        balance = int(response.text) / 1e8  # Convert from Satoshi to BTC
        return balance
    except Exception as e:
        print(f"Error fetching Bitcoin balance: {e}")
        return None

def get_ethereum_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    try:
        response = requests.get(url).json()
        balance = int(response['result']) / 1e18  # Convert from Wei to ETH
        return balance
    except Exception as e:
        print(f"Error fetching Ethereum balance: {e}")
        return None

def format_balance(balance, coin):
    if balance is None:
        return f"\033[91mError\033[0m"
    elif coin == "ETH" and balance < 1e-9:
        return f"\033[93m{balance:.10e} ETH\033[0m"  # Scientific notation for small ETH balances
    else:
        return f"\033[92m{balance:.8f} {coin}\033[0m"  # Normal format for Bitcoin and larger ETH balances

def check_balances(mnemonic):
    btc_address = get_bitcoin_address(mnemonic)
    eth_address = get_ethereum_address(mnemonic)
    btc_balance = get_bitcoin_balance(btc_address)
    eth_balance = get_ethereum_balance(eth_address)

    print(f"\n\033[1mMnemonic:\033[0m \033[96m{mnemonic}\033[0m")
    print(f"  \033[94mBitcoin Address:\033[0m \033[1m{btc_address}\033[0m")
    print(f"  \033[92mBitcoin Balance:\033[0m {format_balance(btc_balance, 'BTC')}")
    print(f"  \033[96mEthereum Address:\033[0m \033[1m{eth_address}\033[0m")
    print(f"  \033[95mEthereum Balance:\033[0m {format_balance(eth_balance, 'ETH')}")
    print("\033[1m" + "-" * 50 + "\033[0m")

def modern_progress_bar(duration=1):
    bar_length = 50  # Length of the progress bar
    start_time = time.time()  # Record the start time
    
    for i in range(101):  # 0 to 100 percentage
        elapsed_time = time.time() - start_time  # Time elapsed since the start
        progress = int((i / 100) * bar_length)
        bar = f"\033[94m[{'▓' * progress}{'░' * (bar_length - progress)}]\033[0m"  # Blue bar with block characters
        sys.stdout.write(f"\r{bar} {i}% Complete")  # Overwrite the same line
        sys.stdout.flush()
        
        # Make the loop run for exactly the specified duration (1 seconds)
        if i != 0:
            time.sleep(duration / 100)  # Adjust sleep time to complete in 1 seconds
    
    sys.stdout.write("\n🎉 \033[92mTask Completed Successfully!\033[0m\n")

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            mnemonics = file.readlines()
            if not mnemonics:
                print("The file is empty. Please provide a file with mnemonic phrases.")
                return
            
            start_time = time.time()  # Start time for measuring the total time
            for index, mnemonic in enumerate(mnemonics, start=1):
                mnemonic = mnemonic.strip()  # Remove extra spaces or newline characters
                if not mnemonic:
                    continue  # Skip empty lines
                
                print(f"\nProcessing Mnemonic {index}:")
                
                if not is_valid_mnemonic(mnemonic):
                    print(f"  \033[1;35mSkipping this mnemonic as it's not BIP39 compliant.\033[0m")
                    print("\033[1m" + "-" * 50 + "\033[0m")
                    continue

                check_balances(mnemonic)  # Process only valid mnemonics
                
            # Measure total duration and update the progress bar
            total_duration = time.time() - start_time
            modern_progress_bar()  # Fixed progress bar with 3 seconds duration
            
    except FileNotFoundError:
        print("\033[1mFile not found.\033[0m Please provide a valid file path.")
    except Exception as e:
        print(f"\033[1mAn error occurred:\033[0m {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[1mUsage:\033[0m python check_multi_coin_balance.py <mnemonic_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

