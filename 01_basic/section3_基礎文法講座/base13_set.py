#　セット

set_a = {1, 2, 3, 4, 5, 5}  # 重複した要素は1つにまとめられる
print(set_a)  # {1, 2, 3, 4, 5}
print('apple' in set_a)  # False
print(3 in set_a)  # True
set_a.add('apple')  # 要素を追加
print(set_a)  # {1, 2, 3, 4, 5, 'apple'}
set_a.remove(2)  # 要素を削除
print(len(set_a))  # セットの要素数を返す 5

# add, remove, discard, pop, clear
set_a.add('e')  # 要素を追加
print(set_a)  # {1, 3, 4, 5, 'apple', 'e'}
set_a.remove('apple')  # 要素を削除  存在しない要素を削除しようとするとエラーになる
print(set_a)  # {1, 3, 4, 5, 'e'}
set_a.discard('banana')  # 存在しない要素を削除しようとするとエラーにならない
val = set_a.pop()  # ランダムに要素を削除して返す
print(val)  # 削除された要素
print(set_a)  # 削除された要素を除いたセット
# set_a.clear()  # セットの全要素を削除
# print(set_a)  # set()

print(type(set_a))  # <class 'set'>
