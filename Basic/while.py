count = 0
while count < 5:
    print(count)
    count += 1

while True:
    age = int(input('あなたは何歳ですか'))
    if not 0 <= age <= 110:
        print('再度入力してください')
        continue
    else:
        print(f'あなたは{age}歳です')
        break
