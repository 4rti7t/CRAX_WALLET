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

⚙️ **INSTALLATION**

```
 git clone https://github.com/4rti7t/CRAX_WALLET.git
 cd CRAX_WALLET
 sudo bash requirements.sh
 python3 crax_wallet.py
```

</br>

<h1 align="center"></h1>

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
![SHUFFLE](https://github.com/user-attachments/assets/b8d4778b-6fc1-486e-aacb-68faae4627d7)


Wallet Balances
![SHUFFLE](https://github.com/user-attachments/assets/0c04a497-799f-44f6-a8be-598c15aa12ea)

**This tool is tested on:**
✅ Ubuntu
✅ Linux Mint
✅ Kali Linux
✅ Fedora
✅ Arch Linux
✅ Parrot Security OS
✅ Windows 11
✅ Termux (Android)

All the new features are primarily tested on Linux, thus Linux is recommended for running PhoneSploit Pro. Some features might not work properly on Windows.
**📋 Notes**
Ensure valid BIP39 mnemonic phrases for correct results.
For enhanced performance, consider multithreading for balance checks.
🤝 Contribution
Feel free to submit issues or pull requests for improvements. For major changes, please open an issue first to discuss your ideas.


**🙌 Acknowledgments**
ASCII Art generated with TAAG.
Progress bar inspired by modern UX principles.

**Developed with ❤️ by @ARTIST for INFLUXION.**
