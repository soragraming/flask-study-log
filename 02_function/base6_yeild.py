# ジェネレータ関数
def generator():
    yield 1
    yield 2
    yield 3

gen = generator() # ジェネレータオブジェクトを作成
print(type(gen))
# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3
# print(next(gen)) # StopIteration ( Error ) yield 4がないため
for i in gen:
    print(i)

# ジェネレータ2
def print_num(max):
    print('ジェネレータ作成')
    for n in range(max):
        print(f'n: {n}')
        yield n

gen = print_num(10)
for i in gen:
    print(f'i: {i}')
# ジェネレータ3 処理を途中からループさせることができ、メモリ使用量の削減

import sys

N = 10**6

def get_list():
    for i in range(N):
        yield i
    # return [i for i in range(N)] # [0, 1,,,999999]

lst = get_list()
print(sys.getsizeof(lst), 'bytes')

# for i in lst:
#     # print(i)