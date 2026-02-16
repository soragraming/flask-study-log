# セットの集合演算

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 和集合
u = s | t
print(u, type(u))  # {'a', 'b', 'c', 'd', 'e', 'f'} <class 'set'>

# 積集合
inter = s & t
print(inter, type(inter))  # {'c', 'd'} <class 'set'>
inter2 = s.intersection(t) # 積集合を求めるメソッド
print(inter2, type(inter2))  # {'c', 'd'} <class 'set'>


# 差集合
diff = s - t
print(diff, type(diff))  # {'a', 'b'} <class 'set'>
diff2 = s.difference(t) # 差集合を求めるメソッド
print(diff2, type(diff2))  # {'a', 'b'} <class 'set'>

# 対称差集合
sym_diff = s ^ t
print(sym_diff, type(sym_diff))  # {'a', 'b', 'e', 'f'} <class 'set'>
sym_diff2 = s.symmetric_difference(t) # 対称差集合を求めるメソッド
print(sym_diff2, type(sym_diff2))  # {'a', 'b', 'e', 'f'} <class 'set'>

# subset, superset
s = {'apple', 'banana', 'cherry'}

t = {'apple', 'banana'}
print(t.issubset(s))  # True
print(s.issuperset(t))  # True
print(s.issubset(t))  # False
print(t.issuperset(s))  # False

print(s <= t)  # False sがtのサブセットであるか
print(t <= s)  # True　tがsのサブセットであるか
print(s >= t)  # True sがtのスーパーセットであるか
print(t >= s)  # False　tがsのスーパーセットであるか

# 重複削除
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4, 5}

# 高速処理 setは中のデータに対して高速に検索できる
large_list = set(range(1000000)) # 0から999999までのリスト
test_number = 999999

import time
start = time.time()
# この処理に何秒かかったか計算
result = test_number in large_list
print(result)

end = time.time()
print('検索時間：', end - start)  # 検索時間： 0.0


