age = 2000
age_alcohol = 20
age_drive = 18

if not 0 < age < 120:
    print('The value is invalid')
elif age >= age_alcohol:
    print('You can drink beer')
elif age < age_drive:
    print('you cannot even drive. ')
else:
    print("You are not allowed to drink beer, but you can drive only if you have a driver's license .")
print('###########')
# if None
a = None
if a is None:
    print('a is None.')
else:
    print('a has value.')
if a:
    print('a has value.')
else:
    print('a is None.')
if not a:
    print('a is None.')

print('###challenge###')
balance = 1000
withdrawal = int(input('引き出し額を入力してください'))
# if withdraw > balance:
#     print(f'残高を超えているため引き出せません。残高は{balance}万円です。')
# else:
#     balance -= withdraw
#     print(f'{withdraw}万円引き出しました。残高は{balance}万円です')

upper_limit = 100
if withdrawal > upper_limit:
    print(f'上限は{upper_limit}万円です。')
elif withdrawal > balance:
    print(f'残高を超えているため引き出せません。残高は{balance}万円です。')
else:
    balance -= withdrawal
    print(f'{withdrawal}万円引き出しました。残高は{balance}万円です')
