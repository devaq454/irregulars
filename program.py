import random

# key = translate. value = tuple(infinitive, past simple, past participle)
dictionary = dict()

for i in open("irregular verbs.txt", 'r'):
    if i.startswith("//"): continue
    words = i.split()
    k = words[0]
    v = tuple(words[1:])
    dictionary[k] = v

keys = list(dictionary.keys())
while True:
    word = random.choice(keys)
    input(word)
    print(*dictionary[word])
