# 変数の応用
animal = 'dog'
動物 = 'cat'
print(動物) # 変数名に日本語も使用可能(一般的には使用しない)

# 定数
LEAGAL_AGE = 20 #定数化で可読性向上
age = 18

if age < LEAGAL_AGE: #ageが20未満の場合処理を実行
    print("未成年です")
else:
    print("成人です")

# format文
print(f'age = {age}') #3.6以降で使用可能
print(f'{age=}')
#3.8以前の場合
print('age = {}'.format(age))
#変数の値を知りたいときに便利
