def get_wordle_guesses():
    words = []
    with open("/Users/jonathankarr/Documents/Python Programming Boot Camp/Course Content/Lessons/More_Content_After_The_Course/Wordle/valid_wordle_guesses.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words

def get_wordle_answers():
    words = []
    with open("/Users/jonathankarr/Documents/Python Programming Boot Camp/Course Content/Lessons/More_Content_After_The_Course/Wordle/valid_wordle_answers.txt", "r") as f:
        for line in f:
            words.append(line.strip())
    return words