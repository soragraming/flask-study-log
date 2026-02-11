#論理型
is_animal = True #Falseでは実行されない
if is_animal:
    print("動物です")

is_man = False
is_adult = True

#or文
if is_man or is_adult: #orはどちらか一方がTrueならTrue
    print("男性または成人です")

#and文
if is_man and is_adult: #andは両方がTrueならTrue
    print("成人男性です")