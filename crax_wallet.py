import sys
import os
import requests
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from eth_account import Account
import random
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Replace with your actual Etherscan API key
ETHERSCAN_API_KEY = '7XX8YH287DCVYQXX7IMMWEIFGMXV1RQ5T5'

# ASCII Art for Menu
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
                        \033[1mразработано @ARTIST для INFLUXION\033[0m
"""

# ASCII Art 2 for Shuffle Phrases
ascii_art_2 = """

   ▄████████    ▄█    █▄    ███    █▄     ▄████████    ▄████████  ▄█          ▄████████ 
  ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ███         ███    ███ 
  ███    █▀    ███    ███   ███    ███   ███    █▀    ███    █▀  ███         ███    █▀  
  ███         ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄      ▄███▄▄▄     ███        ▄███▄▄▄     
▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ███       ▀▀███▀▀▀     
         ███   ███    ███   ███    ███   ███          ███        ███         ███    █▄  
   ▄█    ███   ███    ███   ███    ███   ███          ███        ███▌    ▄   ███    ███ 
 ▄████████▀    ███    █▀    ████████▀    ███          ███        █████▄▄██   ██████████ 
                                                                 ▀                                                                   
                        \033[1mразработано @ARTIST для INFLUXION\033[0m
                        
"""

# ASCII Art 3 for Check Balances
ascii_art_3 = """
██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗    ██████╗  █████╗ ██╗      █████╗ ███╗   ██╗ ██████╗███████╗    
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝██╔════╝    
██║     ███████║█████╗  ██║     █████╔╝     ██████╔╝███████║██║     ███████║██╔██╗ ██║██║     █████╗      
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗     ██╔══██╗██╔══██║██║     ██╔══██║██║╚██╗██║██║     ██╔══╝      
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    ██████╔╝██║  ██║███████╗██║  ██║██║ ╚████║╚██████╗███████╗    
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝    
                        \033[1mразработано @ARTIST для INFLUXION\033[0m
"""

# Utility Functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_mnemonic(mnemonic):
    try:
        return Mnemonic("english").check(mnemonic)
    except Exception:
        return False

def shuffle_phrases():
    clear_screen()  # Clear screen before showing ASCII art and processing
    print("\033[1m" + ascii_art_2)  # Bold ASCII art for Shuffle Phrases
    print(Fore.CYAN + "\033[1mShuffle Phrases: Enter phrases to shuffle.")  # Bold text
    phrases = input(Fore.YELLOW + "\033[1mEnter space-separated mnemonic phrases: ").strip().split()
    
    if len(phrases) < 2:
        print(Fore.RED + "\033[1mError: Please enter at least 2 phrases for shuffling.")
        return
    
    shuffled_results = []
    
    # Shuffle the phrases 144 times and store each shuffled result
    for _ in range(144):
        random.shuffle(phrases)
        shuffled_results.append(" ".join(phrases))
    
    # Show the final shuffled mnemonic (just for reference)
    print(Fore.GREEN + "\033[1mShuffled Mnemonics:")
    for result in shuffled_results:
        print(Fore.CYAN + result)
    
    # Saving the shuffled results to a file
    output_file = input(Fore.YELLOW + "\033[1mEnter the output file path to save shuffled phrases: ").strip()
    try:
        with open(output_file, 'w') as file:
            for result in shuffled_results:
                file.write(result + "\n")
        print(Fore.GREEN + f"\033[1mShuffled mnemonics saved to: {output_file}")
    except Exception as e:
        print(Fore.RED + f"\033[1mError saving to file: {e}")
    
    # Show the modern progress bar after shuffling
    modern_progress_bar(duration=3)


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
    else:
        return f"\033[92m{balance:.8f} {coin}\033[0m"

def modern_progress_bar(duration=5):
    for i in range(101):
        bar = "\033[94m[" + "#" * (i // 2) + "-" * (50 - (i // 2)) + "]\033[0m"
        print(f"\r{bar} {i}%", end="")
        time.sleep(duration / 100)
    print("\n")

# Main Menu Functionality
def menu():
    while True:
        clear_screen()  # Clear screen at the start of each new option selection
        print(ascii_art)
        print(Fore.CYAN + "\nCryptocurrency Wallet Utility")
        print(Fore.YELLOW + "1. Shuffle Mnemonic Phrases")
        print(Fore.YELLOW + "2. Check Wallet Balances")
        print(Fore.YELLOW + "3. Exit\n")
        
        choice = input(Fore.GREEN + "Choose an option: ")
        
        if choice == '1':
            shuffle_phrases()
        elif choice == '2':
            check_balances_menu()
        elif choice == '3':
            print(Fore.RED + "Exiting the program.")
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")

def check_balances_menu():
    clear_screen()  # Clear screen before showing ASCII art and processing
    print(ascii_art_3)  # Print third ASCII art for Check Balances
    print(Fore.CYAN + "Checking balances for your cryptocurrency wallets...")
    file_path = input(Fore.YELLOW + "Enter the file path for mnemonic phrases: ").strip()
    
    try:
        with open(file_path, 'r') as file:
            mnemonics = file.readlines()
            if not mnemonics:
                print(Fore.RED + "Error: The file is empty. Please provide a file with mnemonic phrases.")
                return
            
            start_time = time.time()
            for index, mnemonic in enumerate(mnemonics, start=1):
                mnemonic = mnemonic.strip()
                if not mnemonic:
                    continue
                
                print(f"\nProcessing Mnemonic {index}:")
                if not is_valid_mnemonic(mnemonic):
                    print(Fore.MAGENTA + "Skipping invalid BIP39 mnemonic.")
                    continue
                
                btc_address = get_bitcoin_address(mnemonic)
                eth_address = get_ethereum_address(mnemonic)
                btc_balance = get_bitcoin_balance(btc_address)
                eth_balance = get_ethereum_balance(eth_address)

                print(Fore.BLUE + f"  Bitcoin Address: {btc_address}")
                print(Fore.GREEN + f"  Bitcoin Balance: {format_balance(btc_balance, 'BTC')}")
                print(Fore.CYAN + f"  Ethereum Address: {eth_address}")
                print(Fore.MAGENTA + f"  Ethereum Balance: {format_balance(eth_balance, 'ETH')}")
                print(Fore.YELLOW + "-" * 50)
            
            modern_progress_bar(duration=3)
    
    except FileNotFoundError:
        print(Fore.RED + "Error: File not found. Please provide a valid file path.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

# Run the Menu
if __name__ == "__main__":
    menu()
