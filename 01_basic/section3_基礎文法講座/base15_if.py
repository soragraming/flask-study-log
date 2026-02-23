var = True

if var: #この中の式がTrueの場合実行される
    print('varはTrueです。この中は実行されます。')

age = 20
print(bool(age)) # True
if age: #0以外はTrue
    print(f'ageは{age}です。この中は実行されます。')

msg = 'Hello'
if msg: #msgが空白でない場合はTrueに変換
    print(f'msg:{msg}')

# 数値は0，0.0，文字列，リスト，辞書,タプル,セットは空の場合False

fruits = ['apple','lemon']
if fruits:
    print(f'fruitsの中身は:{fruits}')

age = 20
print(age >= 20)

if age >= 20: #ageが20以上の場合、True
    print('成人です')

x = 5
if x == 5: # ==は一致するかの確認　!=は逆
    print('xは５です')

