if name := input('名前を入力：'):
    print(f'こんにちは、{name}')

numbers = [1, 2, 3, 4, 5]
if (length := len(numbers)) >= 3:
    print(length)

if (n := int(input('数値：'))) > 100:
    print(f'{n}の2倍：{n * 2}')

while(line := input('入力：')) != 'quit':
    print(f'入力 {line}')

data = ['line1', 'line2', 'line3', '']
i = 0
while line := data[i] if i < len(data) else '':
    print(line)
    i += 1

# セイウチ
# for i in range(1, 101):
#     # あまりを計算しつつ判定
#     rem3 := i % 3
#     rem5 := i % 5
    
#     if rem3 == 0 and rem5 == 0:
#         print(f'{i}は15の倍数')
#     elif rem3 == 0:
#         print(f'{i}は3の倍数')
#     elif rem5 == 0:
#         print(f'{i}は5の倍数')
#     else:
#         print(i)