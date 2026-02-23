# 少数
a = 3.14
b = 3.0
c = -10.0

print(a, b, c)
print(type(a), type(b), type(c))

x = 10.5
y = 3.2
print(x + y)
print(x - y)
print(x * y)
print(x / y)  # 割り算
print(x // y) # 切り捨て除算
print(x % y)  # 剰余
print(x ** y) # べき乗

x = 0.01
y = 0
for _i in range(100):
    y += x
print(y)  # 浮動小数点数の誤差に注意