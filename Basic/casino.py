casino_age = 18
age = int(input('何歳ですか'))
casino_game = {1: 'ルーレット',  2: 'ブラックジャック', 3: 'ポーカー'}

if age >= casino_age:
    print('どうぞお入りください。')
    while True:
        print('ゲームを選択してください')
        for num, game in casino_game.items():
            print(f'{num}:{game}')
        play_game = int(input(f'Number:'))
        if play_game in casino_game:
            print(f'あなたは{casino_game[play_game]}を選択しました。')
            break
        else:
            print('リストから選択してください')

else:
    print(f'入店は{casino_age}歳以上からになります。')
