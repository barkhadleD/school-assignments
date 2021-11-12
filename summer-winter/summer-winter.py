# This program is a sample program using nested if statements

print('Hello. My name is Com Puter. What is your name?')
Name = input().capitalize()

print(f'It is good to meet you, {Name}')
print()

print('I would like to ask you a question.')
print()

print(f'do you like winter or summer the best {Name}?')
season = input ()

if season == ('summer'):
    print('I like summer the best as well')
    print('Do you ever find that summer is too hot')
    print('Please answer yes or no')
    hot = input ()

    if hot == ('no'):
        print('Me either. You will never hear me complain')
        print ('about the weather being too hot in the summer time.')

    elif hot == ('yes'):
        print('''I find that interesting. you said that you find summer
        to be hot but yet you also said that summer was your favourite 
        time of year.''')


if season == ('winter'):
    print('Don\'t you find winter too cold?')
    print('Please answer yes or no.')
    cold = input()

    if cold == ('no'):
        print ('I think you are crazy. I don\'t know how stay warm')
        print()
        print(f'it\'s been nice chatting with you {Name}')
        print('I hope we get the chance to chat again soon, ')  
          
    elif cold == ('yes'):
        print('I agree winter is really cold that is why i bought a jacket.')
        print()
        print(f'Thank you {Name} for talking to me')
        print('We should talk more next time')

#------------------------------------------------------------------------------
if season == ('Summer'):
    print('I like summer the best as well')
    print('Do you ever find that summer is too hot')
    print('Please answer yes or no')
    hot = input ()

    if hot == ('no'):
        print('Me either. You will never hear me complain')
        print ('about the weather being too hot in the summer time.')

    elif hot == ('yes'):
        print('''I find that interesting. you said that you find summer
        to be hot but yet you also said that summer was your favourite 
        time of year.''')


if season == ('Winter'):
    print('Don\'t you find winter too cold?')
    print('Please answer yes or no.')
    cold = input()

    if cold == ('no'):
        print ('I think you are crazy. I don\'t know how stay warm')
        print()
        print(f'it\'s been nice chatting with you {Name}')
        print('I hope we get the chance to chat again soon, ')  
          
    elif cold == ('yes'):
        print('I agree winter is really cold that is why i bought a jacket.')
        print()
        print(f'Thank you {Name} for talking to me')
        print('We should talk more next time')

print(f'I must go now {Name}. Goodbye.')
# to fix the cap problem maybe you should .capitalize()
