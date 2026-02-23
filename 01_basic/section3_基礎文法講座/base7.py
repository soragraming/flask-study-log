#文字列

fruit = "Apple"
print(fruit, type(fruit))
# print(dir(fruit)) # 文字列が持つメソッド一覧を表示
print(fruit.lower())  # 小文字に変換
fruit_10 = fruit * 10
print(fruit_10)
# print(fruit * 10)  # 文字列の繰り返し

number = '10'
print(number * 5)

new_fruit = fruit + " Banana" #連結
print(new_fruit)

# """,'''
fruits = """Apple
Banana
grape"""

print(fruits) #|nで改行される
fruits = 'Apple\nBanana\ngrape'
print(fruits)

fruit = 'banana'
print(fruit[1], fruit[0], fruit[-1])  # インデックス指定で文字を取得

print("="*30) # encode,decode(bytesへ変換)
message = "こんにちは"
message_content = message.encode("utf-8")
print(message_content)
print(message_content.decode("utf-8"))

# countメソッド
msg = "ABCDEFABCDEFG"
result = msg.count("A")  # 文字Aの出現回数をカウント
print(result)

# startwith, endswithメソッド
print(msg.startswith("ABC"))  # 文字列が"ABC"で始まるか
print(msg.endswith("ABC"))    # 文字列が"ABC"で終わる

# strip, lstrip, rstripメソッド
print(msg.strip("A"))  # 文字列の両端から"A"を削除
print(msg.lstrip("A")) # 文字列の左端から"A"を削除
print(msg.rstrip("G")) # 文字列の右端から"G"を削除

print("   Hello   ".strip())  # 引数なしで空白を削除 1番使うかも？

# upper, lower, swapcase, replace, capitalizeメソッド
msg = "Hello World"
msg_u = msg.upper()          # 大文字に変換 HELLO WORLD
msg_l = msg.lower()          # 小文字に変換 hello world
msg_s = msg.swapcase()       # 大文字と小文字を入れ替え hELLO wORLD
msg_r = msg.replace("World", "Python")  # 文字列を置換 Hello Python
msg_c = msg.capitalize()     # 先頭文字を大文字に変換 Hello world

print(msg_u, msg_l, msg_s, msg_r, msg_c)
# print(dir(msg))  # 文字列が持つメソッド一覧を表示

# isupper, islower, isdigit, isalphaメソッド
name = "sora, そら"
age = "30"
print(name.isupper())  # すべて大文字か False
print(name.islower())  # すべて小文字か True
print(name.isdigit())  # すべて数字か False
print(name.isalpha())  # すべてアルファベットか False
print(age.isdigit())   # すべて数字か True
print(age.isalpha())   # すべてアルファベットか False

# 検索find, rfind, index, rindexメソッド
msg = "ABCDEFABCDEFG"
print(msg.find("A"))    # 文字Aの最初のインデックスを取得 0
print(msg.rfind("A"))   # 文字Aの最後のインデックスを取得 6
print(msg.index("B"))   # 文字Bの最初のインデックスを取得 1
print(msg.rindex("B"))  # 文字Bの最後のインデックスを取得 7

# index: 存在しない文字を検索するとエラーになる
# print(msg.index("Z"))  # ValueError: substring not found
# find: 存在しない文字を検索すると-1を返す
print(msg.find("Z"))    # -1

# 文字列スライシング
msg = "0123456789"
print(msg[2:5])    # インデックス2から5の手前まで 234
print(msg[:5])     # インデックス0から5の手前まで 01234
print(msg[5:])     # インデックス5から最後まで 56789
print(msg[-4:-1])  # インデックス-4から-1の手前まで 678
print(msg[::2])    # インデックス0から最後まで2つ飛ばし 02468
print(msg[1::2])  # インデックス1から最後まで2つ飛ばし 13579
print(msg[::-1])   # 文字列を逆順に表示 9876543210

# 一度スライスしたものに対して、さらにスライス（ステップ）をかける
msg_sliced = msg[2:8]
msg_skipped = msg_sliced[::2]
print(msg_sliced)  # 234567
print(msg_skipped) # 246