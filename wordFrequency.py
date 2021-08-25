from typing import Counter

input_string = input()
words = input_string.split()
words.sort()
word_count = dict(Counter(words))

for word in word_count:
    print("{}:{}".format(word, word_count[word]))
