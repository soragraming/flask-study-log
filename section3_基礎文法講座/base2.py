# 変数の応用
animal = 'dog'
動物 = 'cat'
print(動物)

# 定数

LEAGAL_AGE = 20
age = 18

if age < LEAGAL_AGE:
    print("未成年です")
else:
    print("成人です")
    

# format文
print(f'age = {age}') #3.6以降で使用可能
#3.8以前の場合
print('age = {}'.format(age))