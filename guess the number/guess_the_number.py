#Guess The Number Game
#Your Name Goes Here: Jibril Derie
#Today's Date Goes Here: 12/10/21

import random
guessesTaken = 0
randomNumber = random.randint(1, 20)
repeat = ('Yes')
while repeat == ('Yes'):
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
            if triesLeft > 1:
                print(f'''Ok {yourName} you have {triesLeft} guesses .
What number do you think im thinking of?''')
            elif triesLeft == 1:
                print(f'''Ok {yourName} you only have 1 guess.
What number do you think im thinking of?''')
            userGuess = input()
            userGuess = int(userGuess)
            guessesTaken = guessesTaken +1
            if guessesTaken > 1 and userGuess == randomNumber:
                guessesTaken = str(guessesTaken)
                print(f'''Good job, {yourName}! You guessed my number in {guessesTaken}
guesses.''')
                print('would you like to play again. Please answer with Yes on No.')
                repeat = input().capitalize()
                break
            elif guessesTaken == 1 and userGuess == randomNumber:
                guessesTaken = str(guessesTaken)
                print(f'''Good job, {yourName}! You guessed my number in {guessesTaken}
guess.''')
                print('would you like to play again. Please answer with Yes on No.')
                repeat = input().capitalize()
                break
            elif userGuess > 20 or userGuess < 1:
                print('''Your guess should not be higher then 20 or smaller then 1,
the number is inbetween 1 and 20 so try to get within that range.''')  
            elif userGuess < randomNumber:
                print('Your guess is to low')
            elif userGuess > randomNumber:
                print('Your guess is too high')
        if userGuess != randomNumber:
            randomNumber = str(randomNumber)
            print(f'''You are out of guesses. The number I was thinking was
    {randomNumber}.''')
        print('would you like to play again. Please answer with Yes on No.')
        repeat = input().capitalize()
