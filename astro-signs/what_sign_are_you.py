#NOTES:
#Dont forget to add the else statement if for example the user spell the       
#month wrong or adds any value that is not added in the code.



print('Hello my name is Com Puter, what is you name?.')
name = input().capitalize()
print()
print(f'{name} would you like to know your astrological sign?')
print('Please answer with yes or no.')
yes = input()
if yes == ('yes'):
    print(f'Ok {name} please enter your birth month')
    birthMonth = input().capitalize()

    
    if birthMonth == ('January'):
        print('''which day in Janurary where you born? please enter only the
number for example if you where born on january 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 19:
            print(f'{name}, Your astrological sign is Capiricorn.')
        elif birthDay > 19 :
            print(f'{name}, Your astrological sign is Aquarius.')

            
    if birthMonth == ('February'):
        print('''which day in February where you born? please enter only the
number for example if you where born on February 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 18:
            print(f'{name}, Your astrological sign is Aquarius.')
        elif birthDay > 18:
            print(f'{name}, Your astrological sign is Pisces.')

            
    elif birthMonth == ('March'):
        print('''which day in March where you born? please enter only the
number for example if you where born on March 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 20:
            print(f'{name}, Your astrological sign is Pisces.')
        elif birthDay > 20:
            print(f'{name}, Your astrological sign is Aries.')

            
    elif birthMonth == ('April'):
        print('''which day in April where you born? please enter only the
number for example if you where born on April 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 20:
            print(f'{name}, Your astrological sign is Aries.')
        elif birthDay > 20:
            print(f'{name}, Your astrological sign is Taurus.')

        
    elif birthMonth == ('May'):
        print('''which day in May where you born? please enter only the
number for example if you where born on May 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 20:
            print(f'{name}, Your astrological sign is Taurus.')
        elif birthDay > 20:
            print(f'{name}, Your astrological sign is Gemini.')

        
    elif birthMonth == ('June'):
        print('''which day in June where you born? please enter only the
number for example if you where born on June 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 21:
            print(f'{name}, Your astrological sign is Gemini.')
        elif birthDay > 21:
            print(f'{name}, Your astrological sign is Cancer.')

        
    elif birthMonth == ('July'):
        print('''which day in July where you born? please enter only the
number for example if you where born on July 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 22:
            print(f'{name}, Your astrological sign is Cancer.')
        elif birthDay > 22:
            print(f'{name}, Your astrological sign is Leo.')

        
    elif birthMonth == ('August'):
        print('''which day in August where you born? please enter only the
number for example if you where born on August 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 22:
            print(f'{name}, Your astrological sign is Leo.')
        elif birthDay > 22:
            print(f'{name}, Your astrological sign is Virgo.')

        
    elif birthMonth == ('September'):
        print('''which day in September where you born? please enter only the
number for example if you where born on September 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 22:
            print(f'{name}, Your astrological sign is Virgo.')
        elif birthDay > 22:
            print(f'{name}, Your astrological sign is Libra.')

        
    elif birthMonth == ('October'):
        print('''which day in October where you born? please enter only the
number for example if you where born on October 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 24:
            print(f'{name}, Your astrological sign is Libra.')
        elif birthDay > 24:
            print(f'{name}, Your astrological sign is Scorpio.')

        
    elif birthMonth == ('November'):
        print('''which day in November where you born? please enter only the
number for example if you where born on November 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 23:
            print(f'{name}, Your astrological sign is Scorpio.')
        elif birthDay > 23:
            print(f'{name}, Your astrological sign is Sagittarius.')

            
    elif birthMonth == ('December'):
        print('''which day in December where you born? please enter only the
number for example if you where born on December 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 21:
            print(f'{name}, Your astrological sign is Sagittarius.')
        elif birthDay > 21:
            print(f'{name}, Your astrological sign is Capricorn.')

            
    else:
        print('L')

        
else:
    print(f'''Ok {name} if you ever want to know your astrological sign let me
know.''')
