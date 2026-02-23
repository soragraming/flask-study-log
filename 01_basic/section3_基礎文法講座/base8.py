# int, str型への変換
int_num = 12
str_num = str(int_num)
print(str_num, type(str_num))
print('num = ' + str(int_num))
float_num = 3.14
str_float = str(float_num)
print(str_float, type(str_float))

# str型からint, float型へ変換
str_int = '100'
int_msg = int(str_int)
float_msg = float(str_int)
print('value = {}, type = {}'.format(int_msg, type(int_msg)))
print('value = {}, type = {}'.format(float_msg, type(float_msg)))