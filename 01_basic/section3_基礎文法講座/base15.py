# --- 1. ミュータブル（リスト）の実験 ---
list_a = ['a', 'b']
list_b = list_a      # 同じ「実体」を指すようにする
list_a.append('c')   # 実体を直接書き換える

print(list_a) # ['a', 'b', 'c']
print(list_b) # ['a', 'b', 'c'] ← 連動して変わった！これがミュータブル。

# --- 2. イミュータブル（タプル）の実験 ---
tuple_a = ('a', 'b')
tuple_b = tuple_a
# tuple_a[0] = 'z'   # ← ここでエラーが出る！「書き換え不可」だから。

tuple_a = ('x', 'y') # これは「新しいタプル」の再代入（作り直し）
print(tuple_a) # ('x', 'y')
print(tuple_b) # ('a', 'b') ← tuple_bは「古い実体」を指したまま。連動しない！