class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # ①<__main__.Vector object at 0x1046a3e50>
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self): # __str__:①を人間に読みやすい形に変更
        return f'x: {self.x}, y: {self.y}'

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2 # v1.__add__(v2)
print(v3) #x: 4, y: 6
v4 = str(v3)
print(v4)

print(Vector.__name__) #Vector 文字列として取得
print(v3.__class__.__name__)

# Gemini補習
class Car:
    def __init__(self, model):
        self.model = model

    # print(car) した時に表示される内容を決める
    def __str__(self):
        return f"この車は {self.model} です"

    # len(car) した時に返る値を決める（例：モデル名の文字数）
    def __len__(self):
        return len(self.model)

car = Car("Prius")

print(car)      # 魔法発動！ -> この車は Prius です
print(len(car)) # 魔法発動！ -> 5