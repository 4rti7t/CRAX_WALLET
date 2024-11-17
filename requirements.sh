#!/bin/bash

# Install Python3 and pip
echo -e "\033[1;32mInstalling Python3 and pip...\033[0m"
sudo apt install -y python3 python3-pip

# Install required libraries
echo -e "\033[1;32mInstalling required libraries...\033[0m"
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

# Install Python dependencies
echo -e "\033[1;32mInstalling Python dependencies...\033[0m"
pip3 install requests mnemonic bitcoinlib eth-account colorama

# Done
echo -e "\033[1;32mAll dependencies have been installed successfully!\033[0m"

