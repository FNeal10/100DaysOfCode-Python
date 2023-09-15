import random
import Hangman_Art
import Stages
import Words


print(Hangman_Art.welcome)
print(Hangman_Art.logo)


display_word = []
random_word = random.choice(Words.word_list)
user_lives = 6

for let in random_word:
    display_word.append('_')

while True:
    if '_' in display_word:
        guess_letter = input("Provide a letter: ")
        if guess_letter.lower() in random_word:
            for inx, val in enumerate(random_word):
                if guess_letter == val:
                    display_word[inx] = val
            print("Letter in word")
            print(''.join(display_word))
        else:
            user_lives -= 1
            print("Letter not in word")
            print(Stages.stages[user_lives])

        if user_lives == 0:
            print(f"No more lives left. The correct word is {random_word}")
            break
    else:
        print("You guessed the word!\nThank You")
        break
