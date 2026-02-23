# tuple型　データ型です。リストと似ていますが、タプルは変更不可（immutable）であるため、要素の追加や削除ができない
fruits = ('apple', 'banana', 'orange') # タプルは()で定義

print(fruits, type(fruits), fruits[0]) # ('apple', 'banana', 'orange') <class 'tuple'> 'apple'

# 要素の追加
fruits = fruits + ('grape',)
print(fruits) # ('apple', 'banana', 'orange', 'grape')

list_fruits = list(fruits)  # タプルをリストに変換
list_fruits.append('melon')  # リストに要素を追加
print(list_fruits, type(list_fruits))  # ['apple', 'banana', 'orange', 'grape', 'melon'] <class 'list'>

# タプルのメソッド  使用頻度は低い
print(fruits.count('apple'))  # タプル内の'apple'の出現回数をカウント
print(fruits.index('banana'))  # タプル内の'banana'のインデックスを返す

cordinate = (10, 20)
# longtitude  cordinate[0] #軽度
# latitude = cordinate[1]　#緯度


logitude, latitude = cordinate  # タプルのアンパック
print(logitude, latitude, type(logitude), type(latitude))  # 10 20 <class 'int'> <class 'int'>

# 辞書のキー
countries = { cordinate: 'Japan' }
print(countries)  # {(10, 20): 'Japan'}

# リストはミュータブル（変更可能）　要素数が変わる可能性がある為、余分なメモリ領域を確保する必要がある
# タプルはイミュータブル（変更不可）　サイズ固定の為。作成時に必要なメモリだけを確保して効率的に使用できる


