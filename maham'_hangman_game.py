
"""#code with multiple words & graphics"""

#code with multiple word string
#Game consist of 5 words, if you guessed the first word right, it will ask you to guess the 2nd word untill you reach total 5 letter.
# however if you typed a wrong letter of gussing word, it will tell you how many wrong try limites your left with.
#if you reach the limit of wrong guess 'game will end'



import random  #to shuffle the list of words randomly

words = ["berlin", "paris", "london", "tokyo", "newyork"]
random.shuffle(words)  # Shuffle the list of words

def select_next_word():
    return words.pop() if words else None #if list is not empty yet , it will pop the last word

word = select_next_word() # Select the first word from the list
hidden_word = []
max_attempts = 6
attempts = 0

hangman = {
    0: '''
        ____________
         |
         |
         |
         |
         |
    ''',
    1: '''
        ____________
         |
         |
         |
         |
         |
    O''',
    2: '''
        ____________
         |
         |
         |
         |
         |
        O/''',
    3: '''
        ____________
         |
         |
         |
         |
         |
        O/ \\''',
    4: '''
        ____________
         |
         |
         |
         |
         |
        O/ \\
         |''',
    5: '''
        ____________
         |
         |
         |
         |
         |
        O/ \\
         |
        /''',
    6: '''
        ____________
         |
         |
         |
         |
         |
        O/ \\
         |
        / \\'''
}  #hangman dictionary which stores ghraphics represent wrong number of attempts

print("Welcome to Hangman Game!") #first display
print("****Guess the word***")

while True:
    display = ""  #if the guess is right then word/letter will append to variable display otherwise it will display '-'
    for letter in word:
        if letter in hidden_word:
            display += letter
        else:
            display += "_ "

    print(display)

    if display == word:
        print("Awesome! You've guessed the word:", word)
        print("  \U0001f600  \U0001f600   \U0001f600  ") #emoji code :)
        word = select_next_word() # Move to the next word after successfully guessing the current word
        hidden_word = [] # Reset hidden_word for the new word

        if not word: #when user have guessed all the words from list
            print("Congratulations! You've guessed all the words!") #game end
            print("     \U0001F643 \U0001F929 \U0001F643 ")
            break

        print("\nGuess the next word:")
        attempts = 0  # Reset the attempts counter for the new word
        continue

    if attempts >= max_attempts: #when number of wrong attempts will reach max '6'
        print("Game Over! The word was:", word)
        print(hangman[6]) #hangman graphic steps from 1 to 6
        print('HANGED!!!') #games ends after attempt limit reached
        print(' \U0001FAE3 \U0001FAE3 \U0001FAE3 \U0001FAE3 \U0001FAE3') #emoji code
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha(): #to make sure user only enter alphabetic letters
        print("Please enter a single letter.") #if user enter more than one letters or any other string type
        continue

    if guess in hidden_word: #to check if the user have guessed this letter already
        print("You've already guessed that letter.")
        continue

    hidden_word.append(guess) #replace '-' with right guess

    if guess not in word: #number of attempts
        attempts += 1
        print("Wrong guess!!!")
        print(hangman[attempts])
        attempts_left = max_attempts - attempts
        print("Only Numbers of Attempts left is", attempts_left)
