# 練習問題
# numという変数に数値の10を格納してください
# numの型を標準出力してください
# 演習2のnumを文字列に変換して、num_strという変数に格納してください
# リストnum_listにnum_strと“20”, “30”を格納してください
# num_listに新たに要素“40”を格納してください
# num_listをタプルに変換したnum_tupleを作成してください
# 標準入力を受け付けて、num_tupleに追加してください。
# セットnum_setを作成して、要素は「40」, 「50」, 「60」にしてください
# num_tupleとnum_setのユニオン（和集合）を表示してください
# 辞書型、num_dictをキーをnum_tuple、値をnum_strとして作成
# リストnum_listの長さ（要素数）を表示してください
# num_dictからキー’MyKey’の値を取り出し、見つからない場合は‘Does not exist’を標準出力してください
# リストnum_listに「50」, 「60」を新たに一行で追加してください。
# 標準入力を受け付け、is_under_50という論理型の変数に受け付けた標準入力が50より小さいかを入れてください
# num_str = {num_strの値}として標準出力してください
# num_dictが持っている属性とメソッド一覧を標準出力してください。


num = 10
print(type(num))
num_str = str(num)

num_list = [num_str,'20', '30']
num_list.append('40')
num_tuple = tuple(num_list)

val = input('追加する値を入力してください：')
num_tuple = num_tuple + (val,)

# print(num_tuple)

num_set = {'40', '50', '60'}
print(set(num_tuple) | num_set)

num_dict = {num_tuple: num_str}

print(len(num_list))
print(num_dict.get('MyKey', 'Does not exist'))

num_list.extend(['50', '60'])

val = input('数値を入力してください：')
is_under_50 = int(val) < 50
print(f'is_under_50 = {is_under_50}')
print(f'num_str = {num_str}')
print(dir(num_dict))