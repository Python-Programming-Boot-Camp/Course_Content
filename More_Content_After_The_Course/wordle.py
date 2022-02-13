words = []
with open('More_Content_After_The_Course/valid_wordle_answers.txt') as file:
    for line in file: 
        words.append(line.strip())

def play_wordle(words : list) -> None:
    """ Eliminate words"""
    while len(words) > 1:
        letters_in_word = []
        for position in range(5):
            letter=input("What letter did you put in position " + str(position + 1) + "?: ").lower()
            color=input("What color is it? (Y,G,B): ")
            if color.lower() != 'g' and color.lower() != 'y' and color.lower() != 'b':
                print("invalid input please start over")
                return
            words_to_remove = []
            for word in words:
                if color.lower() == 'g':
                    if word[position] != letter:
                        words_to_remove.append(word)
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
                elif color.lower() == 'b':
                    if letter in word:
                        if letter not in letters_in_word:
                            words_to_remove.append(word)
                        elif word[position] == letter:
                            words_to_remove.append(word)
                elif color.lower() == 'y':
                    if letter not in word:
                        words_to_remove.append(word)
                    elif word[position] == letter:
                        words_to_remove.append(word)
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
            for word in words_to_remove:
                words.remove(word)
        print(words)
        guess = input("Did you guess correctly (Y/N)?: ")
        if guess.lower() == "y":
            print("Congrats you got it!")
            return
play_wordle(words)