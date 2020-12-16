user_word = input("Enter a word: ")
user_word = user_word.upper()
word = ""
for letter in user_word:
    if (letter in "AEIOU"):
        continue
    word += letter
print(word)