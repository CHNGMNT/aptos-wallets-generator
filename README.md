# aptos-wallets-generator

Софт генерирует адрес и приватник по-умолчанию

Чтобы генерировать с seed-фразой поменять местами функции 'def generate_wallets(num_wallets):' и раскоментить все остальное(у меня почему-то не устанавливается bip_utils, поэтому я ее отключил)

'requirements.txt' установить библиотеки и в файле data.py указать путь до папки с aptos-sdk

В main.py указываем количество кошельков и запускаем

После запуска создается папка results вместе с private_keys.txt, addresses.txt и wallets.csv
