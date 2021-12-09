# Guess The Number Game
# Your Name Goes Here
#Today's Date Goes Here

import random

guessesTaken = 0

randomNumber = random.randint(1, 20)
print(f'''Hello my name is Com Puter, we are going to play a game where you
guess the number I am thinking of That's inbetween 1 and 20. We will start the
game with you choosing the amount of guesses that you would want to take at
most. Lets start with your name.
What is your name?''')
yourName = input().capitalize()

print('How many guesses would you like to have.')
tries = int(input())

while guessesTaken < tries:

    triesLeft = tries - guessesTaken

    print(f'''Ok {yourName} the amount of times you can guess is {triesLeft}.
What number do you think im thinking of?''')### If you have one guesse left it says 1 guesses left fix that.
    userGuess = input()
    userGuess = int(userGuess)

    guessesTaken = guessesTaken +1

    if userGuess == randomNumber:
        guessesTaken = str(guessesTaken)
        print(f'''Good job, {yourName}! You guessed my number in {guessesTaken}
guesees!''')
        break

    elif userGuess > 20:
        print('''Your guess should not be higher then 20 the number is inbetween
1 and 20 so try to get within that range.''')
        
    elif userGuess < randomNumber:
        print('Your guess is to low')

    elif userGuess > randomNumber:
        print('Your guess is too high')
    
if userGuess != randomNumber:
    randomNumber = str(randomNumber)
    print(f'''You are out of guesses. The number I was thinking was
{randomNumber}.''')


