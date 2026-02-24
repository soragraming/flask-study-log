# イミュータブルな方は関数内で変更しても外には影響がない
def try_modify_number(num):
    num += 10
    print(f'関数内: {num}')

x = 5
try_modify_number(x) #関数内: 15
print(x) # 5

# ミュータブルは影響あり
def try_modify_list(numbers):
    new_numbers = numbers.copy() # ここで外部に影響しなくなる？
    numbers.append(100)

my_list = [1, 2, 3]
try_modify_list(my_list)
print(my_list) # [1, 2, 3, 100]