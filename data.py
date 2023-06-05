import sys
sys.path.append('C:/Users/Administrator/AppData/Local/Programs/Python/Python310/Lib/site-packages/aptos_sdk')  # указать свой путь до папки
import os
import csv
#from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins
from aptos_sdk.account import Account 
from aptos_sdk.ed25519 import *
from aptos_sdk.account_address import *
from aptos_sdk.bcs import *

def generate_wallets(num_wallets):        #чтобы сгенерировать с seed-фразой удалить эту функцию
    wallets = []
    for _ in range(num_wallets):
        account = Account.generate()
        address = account.address().hex()
        private_key = account.private_key.hex()
        wallets.append({
            'address': address,
            'private_key': private_key,
        })
    return wallets

#чтобы сгенерировать с seed-фразой расскоментить
'''
def generate_wallets(num_wallets):
    wallets = []
    mnemonic_generator = Bip39MnemonicGenerator()

    for _ in range(num_wallets):
        mnemonic = mnemonic_generator.FromWordsNumber(words_num=12)  # Генерация seed-фразы с помощью BIP-39
        seed_generator = Bip39SeedGenerator(mnemonic)
        seed_bytes = seed_generator.Generate()

        bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.APTOS)  # Генерация кошелька Aptos с помощью BIP-44
        account = Account.from_key_pair(bip_obj.PrivateKey().Raw().ToBytes())

        address = account.address().hex()
        private_key = account.private_key.hex()

        wallets.append({
            'address': address,
            'private_key': private_key,
            'mnemonic': mnemonic.split()
        })

    return wallets
'''

def save_wallets_to_files(wallets):
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    addresses_file = os.path.join(results_dir, 'addresses.txt')
    private_keys_file = os.path.join(results_dir, 'private_keys.txt')
    #mnemonics_file = os.path.join(results_dir, 'mnemonics.txt')
    
    with open(addresses_file, 'w') as f_addresses, \
            open(private_keys_file, 'w') as f_private_keys:
            #open(mnemonics_file, 'w') as f_mnemonics:
        for wallet in wallets:
            f_addresses.write(wallet['address'] + '\n')
            f_private_keys.write(wallet['private_key'] + '\n')
            #f_mnemonics.write(' '.join(wallet['mnemonic']) + '\n')


def save_wallets_to_csv(wallets):
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    csv_file = os.path.join(results_dir, 'wallets.csv')

    with open(csv_file, 'w', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['Number', 'Address', 'Private Key', 'Mnemonic'])
        for i, wallet in enumerate(wallets, start=1):
            writer.writerow([i, wallet['address'], wallet['private_key'],])# ' '.join(wallet['mnemonic'])])

text1 = '''
         ___  ___  ___  __   _____    ___  _   _ _____ 
        |  \/  | /   |/  | /  ___|  /   || \ | |  _  |
        | .  . |/ /| |`| | \ `--.  / /| ||  \| | | | |
        | |\/| / /_| | | |  `--. \/ /_| || . ` | | | |
        | |  | \___  |_| |_/\__/ /\___  || |\  \ \_/ /
        \_|  |_/   |_/\___/\____/     |_/\_| \_/\___/ 
  
              https://github.com/vittoriomaisano
              '''

text2= "Генерация кошельков Aptos завершена.\n\nКошельки сохранены в папку 'results'\n"
