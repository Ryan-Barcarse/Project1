"""
Import and download nltk word library
"""
import nltk
nltk.download("words")
from nltk.corpus import words
"""
Initialize is_word to be False and secret_word to be an empty list, print welcome statement
"""
is_word = False
secret_word = [""]
print("Welcome to Wordle - Simple edition!")
"""
Ask the user to input a 5 letter word, check for length of 5 and if it is a valid word in ntlk, then add
into secret_word list, break out of the while loop by setting is_word to True
"""
while is_word == False:
    secret_word[0] = (input("Enter the secret 5-letter word: "))
    if (secret_word[0].lower() in words.words()) and (len(secret_word[0]) == 5):
        is_word = True
    else:
        print("Not a valid word, try again!")
"""
Break up the word into separate letters and put them into the list, removing the original word with pop()
"""
for letter in secret_word[0]:
    secret_word.append(letter)
secret_word.pop(0)
"""
try and except for an integer number, run error message if not in int format
"""
try:
    """
    Initialize N for an int input and attempts to 0
    """
    N = int(input("Input allowed number of attempts: "))
    attempts = 0
    """
    While loop to keep looping if attempts is less than N, make is_word back to false every loop, make player_word an 
    empty list to refresh after every attempt, and add 1 to attempt every loop
    """
    while attempts < (N):
        is_word = False
        player_word = [""]
        attempts += 1
        """
        While loop to check is player_word is valid, ask the user to input a 5 letter word, check for length of 5 and 
        if it is a valid word in ntlk, then add into player_word list, break out of the while loop by setting 
        is_word to True. Also, check for if player_word is over or under 5 letters, and print a warning message
        """
        while (is_word == False):
            player_word[0] = input(f"Enter your attempt #{attempts}: \n")
            if (player_word[0].lower() in words.words()) and (len(player_word[0]) == 5):
                is_word = True
            elif (player_word[0].lower() in words.words()) and ((len(player_word[0]) < 5) or (len(player_word[0]) > 5)):
                print(f"You entered a {len(player_word[0])}-letter word, but a 5-letter word is needed. Try again!")
            else:
                print("Not a valid word, try again!")
        print("You entered a 5-letter word")
        """
        Break up the word into separate letters and put them into the list, removing the original word with pop()
        """
        for letter in player_word[0]:
            player_word.append(letter)
        player_word.pop(0)
        """
        Set counter for how many letters are in the right spot to 0, then check for each letter of player_word
        to see if they match up for each letter of secret_word, if there is a match record the data and print a
        confirmation message, if wrong check if the letter is still in the word and record the data, and print, and
        then check if the player_word is a match to secret_word, break out of the while loop
        """
        letter_in_the_right_spot = 0
        for i in range(len(player_word)):
            for r in range(len(secret_word)):
                if (player_word[i] == secret_word[r]) and (i == r):
                    print(f"{player_word[i]} is in the secret_word and in the correct spot #{i + 1}")
                    letter_in_the_right_spot += 1
                    print(f"Correct letters in the correct spot: {letter_in_the_right_spot}")
                elif player_word[i] in secret_word[r]:
                    print(f"{player_word[i]} is in the secret_word but not in the correct spot")
        if player_word == secret_word:
            break
    """
    Check if the player has reached the amount N attempts, if they guessed the correct word, print congrats message
    if they did not, print better luck again message
    """
    if (attempts <= N) and (attempts != 0) and (player_word == secret_word):
        print(f"Congrats you won using {attempts} attempt(s)")
    elif attempts != 0:
        print(f"You already used #{N} attempts. Better luck tomorrow!")
except ValueError:
    print("Must input an integer!")


