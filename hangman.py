import random


def hangman():
    word_list = ["python", "java", "javascript", "ruby", "swift", "csharp",
                 "flutter", "react", "angular", "vue", "django", "flask", "spring", "laravel"]
    random_word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    print("Let's play Hangman!")
    print('_ ' * len(random_word))

    while attempts > 0:
        guess = input(
            "Please guess a letter of (programming language):").lower()

        if len(guess) != 1:
            print("Please guess only one letter at a time.")
        elif guess in guessed_letters:
            print("You've already guessed this letter.")
        elif guess not in random_word:
            print("Sorry, this letter is not in the word.")
            attempts -= 1
        else:
            print("Good job! That letter is in the word.")
            guessed_letters.append(guess)

        word_so_far = ""
        for letter in random_word:
            if letter in guessed_letters:
                word_so_far += letter + " "
            else:
                word_so_far += "_ "
        print(word_so_far)

        if "_" not in word_so_far:
            print("Congratulations! You've won!")
            return

    print("Sorry, you've run out of attempts. The word was " + random_word + ".")


hangman()
