print("\t\t\tHANGMAN GAME")

import time
time.sleep(1)
print('Let me choose a word')
for i in range(5):
    time.sleep(0.8)
    print(" ? ",end="")
print("\nOk! Im ready!")
time.sleep(0.5)

hangman=['''
|---|---|
|       |
|       |
|       |
|       |
|_______|''',
'''
|---|---|
|   O   |
|       |
|       |
|       |
|_______|''',
'''
|---|---|
|   O   |
|   |   | 
|       |
|       |
|_______|''',
'''
|---|---|
|   O   |
|  \|   |
|       |
|       |
|_______|''',
'''
|---|---|
|   O   |
|  \|/  |
|       |
|       |
|_______|''',
'''
|---|---|
|   O   |
|  \|/  |
|   |   |
|       |
|_______|''',
'''
|---|---|
|   O   |
|  \|/  |
|   |   |
|  /    |
|_______|''',
'''
|---|---|
|   O   |
|  \|/  |
|   |   |
|  / \  |
|_______|''']
import random
words_list = ['absolutely','disaster','collateral','vocabulary','independent']
word = random.choice(words_list)
chances=0
guessed_letter = []
guessed_line=[]
for char in word:
        guessed_line.append('_')
while chances!=7:
        
    user_guess = input("\nPlease guess a letter:")
    user_guess.lower()
    while len(user_guess)>1:
        print("Please enter only 1 letter:")
        user_guess = input("Please guess a letter:")
        user_guess.lower()
    while user_guess.isalpha()!=True:
        print("Please enter only alphabets!")
        user_guess = input("Please guess a letter!")
        user_guess.lower()
    while user_guess in guessed_letter:
        print("You have already guessed this letter!")
        user_guess = input("Please guess a letter!")
        user_guess.lower()
        
    if user_guess in word:
        guessed_letter.append(user_guess)
        print("Guessed Letters : "," ".join(guessed_letter))
        for char in range(len(word)):
            if user_guess==word[char]:
                guessed_line[char]=word[char]
                
        print(hangman[chances])
        print("\n"," ".join(guessed_line))
        
    elif user_guess not in word:
        guessed_letter.append(user_guess)
        print("Guessed Letters : "," ".join(guessed_letter))
        chances+=1
        print(hangman[chances])
        print("\n"," ".join(guessed_line))
    if guessed_line==list(word):
        print("Congratulations!")
        print("You Won!")
        break
else:
    print("YOURE DEAD!")
    print("Idiot, the word was:",word)
    
        
        

