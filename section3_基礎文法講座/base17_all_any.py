# all, any

if all((True, 10 < 20, 'A'=='A')):
    print('allの中を実行')

numbers = [1, 2, 3, 10, 5]
if all(numbers): #すべてTrueの場合だけ実行
    print('0を含みません')

ages = [19, 21, 18, 25, 17]
# [19 >= 18, 21 >= 18, 18 >= 18, 25 >= 18, 17 >= 18]
ages_over_18 = [age >= 18 for age in ages]
print(ages_over_18)
print(all(ages_over_18)) # 1つでもFalseを含んでいるのでFalse

if any((False, False, True)):
    print('anyの中の処理')

print(any(ages_over_18)) #True