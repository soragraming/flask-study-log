# 辞書のメソッド
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2050,
}

tmp_dict = {
    'country': 'Japan',
    'prefedture': 'Aichi',
    "year": 2020,
}
car.update(tmp_dict) # 同じキーがあれば上書き,なければ追加
print(car)
# {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020, 'country': 'Japan', 'prefedture': 'Aichi'}

car['city'] = 'Nagoya'  # cityキーを追加
car['year'] = 2030      # yearキーの値を更新
print(car)
# {'brand': 'Toyota', 'model': 'Corolla', 'year': 2030, 'country': 'Japan', 'prefedture': 'Aichi', 'city': 'Nagoya'}

value = car.popitem()  # 最後に追加された要素を削除して返す
print(value)  # ('city', 'Nagoya')
print(car)
# {'brand': 'Toyota', 'model': 'Corolla', 'year': 2030, 'country': 'Japan', 'prefedture': 'Aichi'}

value = car.pop('model')  # 指定したキーの要素を削除して返す
print(value)  # Corolla
print(car)
# {'brand': 'Toyota', 'year': 2030, 'country': 'Japan', 'prefedture': 'Aichi'}

car.clear()  # 辞書の全要素を削除
print(car)  # {}
del car  # 辞書自体を削除
# print(car)  # NameError: name 'car' is not defined