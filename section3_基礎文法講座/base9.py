# list
list_a = [1, 2, 3,4]
list_b = []

print(list_a)
print(list_a[-2])  # インデックス指定で要素を取得

list_a = [1, [1,2,'apple'],3,'banana']
print(list_a[1][2])
print(list_a)
list_a[1][2] = 'orange'  # 多次元リストの要素変更
print(list_a)


# リストのメソッド
list_a = [1, 2, 3, 4, 5]
list_b = list_a[:3] # スライスでリストの一部を取得
print(list_b) # [1, 2, 3]
print(list_a[0:5:2]) # ステップ指定で要素を取得 [1, 3, 5]
print(list_a[-3:])  # インデックス負数指定で要素を取得 [3, 4, 5]

# appennd, extend, insert, clear
list_a.append('apple')  # リストの末尾に要素を追加
print(list_a)  # [1, 2, 3, 4, 5, 'apple']
list_a.extend(['banana', 'orange'])  # リストを拡張
print(list_a)  # [1, 2, 3, 4, 5, 'apple', 'banana', 'orange']
list_a.insert(2, 'grape')  # インデックス2に要素を挿入
# print(list_a)  # [1, 2, 'grape', 3, 4, 5, 'apple', 'banana', 'orange']
# list_a.clear()  # リストの全要素を削除
# print(list_a)  # []

# remove（1番最初の一致したものを削除、無ければエラー）
# pop (指定したインデックスの要素を削除して返す、無ければ末尾)
# count (要素の出現回数を返す)
# index (要素のインデックスを返す、無ければエラー)
list_a.remove('apple')  # 指定した要素を削除
print(list_a)  # [1, 2, 'grape', 3, 4, 5, 'banana', 'orange']
list_a.pop(2)  # インデックス2の要素を削除し、その要素を返す 26行目　
taken_element = list_a.pop(2)
print(taken_element)  # 3
print(list_a)  # [1, 2, 4, 5, 'banana', 'orange']
print(list_a.count('banana'))  # 要素'banana'の出現回数を返す

print(list_a.index(5))  # 要素5のインデックスを返す
print(list_a.index('orange'))  # 要素'orange'のインデックスを返す

# sort, reverseメソッド
list_c = [5, 2, 9, 1, 5, 6]
list_c.sort()  # リストを昇順にソート
print(list_c)  # [1, 2, 5, 5, 6, 9]
list_c.reverse()  # リストの要素を逆順に並び替え
print(list_c)  # [9, 6, 5, 5, 2, 1]

list_d = ['banana', 'apple', 'orange']
list_d.sort()  # リストをアルファベット順にソート
print(list_d)  # ['apple', 'banana', 'orange']
list_d.reverse()  # リストの要素を逆順に並び替え
print(list_d)  # ['orange', 'banana', 'apple']