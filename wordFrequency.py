from typing import Counter

inputStr = input()
words = inputStr.split()
words.sort()
wordCount = dict(Counter(words))

for word in wordCount:
    print("{}:{}".format(word, wordCount[word]))
