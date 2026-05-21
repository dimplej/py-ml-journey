sentence = "Python programming is very interesting"

largest_word = ""

for word in sentence.split():
    if len(word) > len(largest_word):
        largest_word = word

print(largest_word)