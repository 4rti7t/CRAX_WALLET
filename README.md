# CRAX_WALLET

🚀 **CRYPTO WALLET HACKING TOOL**
A powerful and intuitive tool for cryptocurrency enthusiasts to manage wallets, validate and shuffle mnemonic phrases, and fetch wallet balances for Bitcoin and Ethereum.

🌟 **Features**
🎲 Shuffle Mnemonic Phrases
Validate and shuffle BIP39 mnemonic phrases, saving results to a file.

🔐 **Generate Wallet Addresses**
Generate Bitcoin and Ethereum wallet addresses from valid mnemonic phrases.

💰 **Check Wallet Balances**
Fetch real-time Bitcoin and Ethereum balances for provided wallets using:

Blockchain.info API for Bitcoin.
Etherscan API for Ethereum.

🖼️ **Enhanced User Experience**
Featuring modern ASCII art, a sleek progress bar, and clear feedback.

🛠️ **Requirements**
Ensure the following dependencies are installed:

bash
Copy code
pip install mnemonic bitcoinlib eth_account requests colorama
Python: >= 3.7
Network Access: Required for balance APIs.
API Key: For Ethereum balances, get a free API key from Etherscan.

⚙️ Setup

```
• git clone https://github.com/R3LI4NT/Wifi-Hack
• cd Wifi-Hack
• sudo bash requirements.sh
• python3 wifi-hack.py
```

</br>

<h1 align="center"></h1>

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/crypto-wallet-utility.git
cd crypto-wallet-utility
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add your Etherscan API key in the script:

python
Copy code
ETHERSCAN_API_KEY = 'your_api_key_here'
Run the script:

bash
Copy code
python script_name.py

**📖 Usage**
🎲 Shuffle Mnemonic Phrases
Select Option 1 from the menu.
Enter space-separated mnemonic phrases.
Shuffled results are saved to your specified file.
💰 Check Wallet Balances
Select Option 2 from the menu.
Provide the file path containing mnemonic phrases (one per line).
View addresses and balances for Bitcoin and Ethereum.
📸 Screenshots
Main Menu

Shuffle Phrases

Wallet Balances

**📋 Notes**
Ensure valid BIP39 mnemonic phrases for correct results.
For enhanced performance, consider multithreading for balance checks.
🤝 Contribution
Feel free to submit issues or pull requests for improvements. For major changes, please open an issue first to discuss your ideas.


**🙌 Acknowledgments**
ASCII Art generated with TAAG.
Progress bar inspired by modern UX principles.
**Developed with ❤️ by @ARTIST for INFLUXION.**
