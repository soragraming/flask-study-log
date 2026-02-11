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