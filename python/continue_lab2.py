word_without_vowels = ""

word_entered = input("Enter a word: ")
user_word = word_entered.upper()

for letter in user_word:
    if letter == "A":
        continue
    if letter == "I":
        continue
    if letter == "U":
        continue
    if letter == "E":
        continue
    if letter == "O":
        continue
    else:
        word_without_vowels += letter
        
for letter in word_without_vowels:
    print(letter)