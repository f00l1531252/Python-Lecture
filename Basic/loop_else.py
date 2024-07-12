fruits = ['apple', 'peach', 'banana', 'orange']

for fruit in fruits:
    choice = input(f'あなたが探しているフルーツは{fruit}ですか？ (y/n)')
    if choice == 'y':
        print('見つかってよかったですね')
        break
    else:
        print('....')
else:
    print('お探しのフルーツは見つかりませんでした。')


count = 1
while count < 4:
    print(count)
    count += 1
else:
    print('だーーー')

balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f'一回{game_price}円のゲームに参加しますか(y/n)')
    if choice == 'y':
        balance -= game_price
        print(f'残高は{balance}円です')

    else:
        print('またのご参加をお待ちしております。')
        break
else:
    print(f'あなたの残高は{balance}円です。またのご来店をお待ちしております')