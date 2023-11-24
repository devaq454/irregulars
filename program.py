import random

# key = translate. value = tuple(infinitive, past simple, past participle)
dictionary = dict()

for i in open("irregular verbs.txt", 'r'):
    if i.startswith("//"): continue
    words = i.split()
    k = " ".join(words[:-3])
    v = tuple(words[-3::])
    dictionary[k] = v

keys = list(dictionary.keys())
print(dictionary)
while True:
    word = random.choice(keys)
    input(word)
    print(*dictionary[word])
