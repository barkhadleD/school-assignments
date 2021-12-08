# Guess The Number Game
# Your Name Goes Here
#Today's Date Goes Here

import random

guessesTaken = 0

print('Hello! What is your name?')
yourName = input()

randomNumber = random.randint(1, 20)
print(f'Well {yourName}, I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')
    userGuess = input()
    userGuess = int(userGuess)

    guessesTaken = guessesTaken +1
    
    if userGuess == randomNumber:
        guessesTaken = str(guessesTaken)
        print(f'Good job, {yourName}! You guessed my number in {guessesTaken} guesees!')
        break

    elif userGuess < randomNumber:
        print('Your guess is to low')

    elif userGuess > randomNumber:
        print('Your guess is too high')

if userGuess != randomNumber:
    randomNumber = str(randomNumber)
    print(f'You are out of guesses. The number I was thinking was {randomNumber}.')
