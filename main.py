import random


def read_word():
    words = ["audi", "mercedes", "bmw", "honda", "volkswagen", "toyota", "jeep", "seat"]
    return random.choice(words)


def guess_letter(word, input_letter, guessed_letters):
    new_word = ""
    correct_letter = False
    for letter in word:
        if letter in guessed_letters or letter == input_letter:
            new_word += letter
        else:
            new_word += "*"
        if letter == input_letter:
            correct_letter = True
    return new_word, correct_letter


def game():
    word = read_word()
    guessed_word = "*" * len(word)
    guessed_letters = ""
    number_attempts = int(input("Enter the number of attempts: "))

    while number_attempts > 0:
        print("Guessed word:", guessed_word)
        string = input("Enter a letter or a whole word: ")

        if len(string) == 1:
            if string in guessed_letters:
                print("You have already guessed this letter.")
                continue
            new_word, correct_letter = guess_letter(word, string, guessed_letters)
            if not correct_letter:
                number_attempts -= 1
                print("There is no such letter. Remaining attempts:", number_attempts)
            else:
                guessed_word = new_word
                guessed_letters += string
                if guessed_word == word:
                    print("Congratulations, you guessed the word!")
                    break
        else:
            if string == word:
                print("Congratulations, you guessed the word!")
                break
            else:
                print("The word is not correct, there are still attempts:", number_attempts)
                number_attempts -= 1
    else:
        print("Sorry but you didn't guess the word. The guessed word was:", word)


if __name__ == "__main__":
    print("Game 'Field of wonders'")
    game()g