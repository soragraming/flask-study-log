# リスト内包表記

numbers = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in numbers if x < 3]
print(squares) # [1, 4, 9, 16, 25, 36]

result = [x if x >0 else 0 for x in range(-2, 3)]
print(result) # [0, 0, 0, 1, 2]

# 辞書内包表記
words = ['apple', 'banana', 'cherry']
word_lengths = { word: len(word) for word in words}
