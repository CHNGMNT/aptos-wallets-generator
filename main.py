from data import *
from termcolor import cprint

num_wallets = 5   # Количество кошельков

wallets = generate_wallets(num_wallets)

save_wallets_to_files(wallets)
save_wallets_to_csv(wallets)

if __name__ == '__main__':
    cprint(text1, 'red')
    cprint(text2, 'cyan')
