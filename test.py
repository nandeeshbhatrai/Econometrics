import csv

f = open('bagofwords_ECONOMICTIMES.csv' , 'r')
words = []
for line in f:
    t = line.split(', ')
    words += t

words.sort()
prev = None
g = open('final.csv' , 'w')
for word in words:
    if prev == word:
        continue
    prev = word
    g.write(word.lower() + ", ")


print(words)