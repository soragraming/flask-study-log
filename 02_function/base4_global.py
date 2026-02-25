count = 0 # グローバル変数

def increment():
    # count = 2 # ローカル変数
    global count # グローバルのcountを指す（グローバル宣言）
    count = count + 2 # グローバル変数は書き換えられない
    print('関数内：', count)
    print('関数内(id)：', id(count))

increment()
print('関数内：', count)
print('関数内(id)：', id(count))