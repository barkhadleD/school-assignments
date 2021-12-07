print('Hello my name is Com Puter, what is you name?')
name = input().capitalize()
print()
print(f'{name} would you like to know your astrological sign?')
print('Please answer with yes or no.')
yes = input().capitalize()
if yes == ('Yes'):
    print(f'Ok {name} please enter your birth month.')
    birthMonth = input().capitalize()

    
    if birthMonth == ('January'):
        print('''Which day in Janurary where you born? Please enter only the
number for example if you where born on January 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 19:
            print(f'{name}, your astrological sign is Capiricorn.')
        elif birthDay > 19 and birthDay <= 31:
            print(f'{name}, your astrological sign is Aquarius.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
            
    elif birthMonth == ('February'):
        print('''Which day in February where you born? Please enter only the
number for example if you where born on February 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 18:
            print(f'{name}, your astrological sign is Aquarius.')
        elif birthDay > 18 and birthDay <= 29 :
            print(f'{name}, your astrological sign is Pisces.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
            
    elif birthMonth == ('March'):
        print('''Which day in March where you born? Please enter only the
number for example if you where born on March 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 20:
            print(f'{name}, your astrological sign is Pisces.')
        elif birthDay > 20 and birthDay <= 31:
            print(f'{name}, your astrological sign is Aries.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
            
    elif birthMonth == ('April'):
        print('''Which day in April where you born? Please enter only the
number for example if you where born on April 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 20:
            print(f'{name}, your astrological sign is Aries.')
        elif birthDay > 20 and birthDay <= 30:
            print(f'{name}, your astrological sign is Taurus.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('May'):
        print('''Which day in May where you born? Please enter only the
number for example if you where born on May 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 20:
            print(f'{name}, your astrological sign is Taurus.')
        elif birthDay > 20  and birthDay <= 31:
            print(f'{name}, your astrological sign is Gemini.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('June'):
        print('''Which day in June where you born? Please enter only the
number for example if you where born on June 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 21:
            print(f'{name}, your astrological sign is Gemini.')
        elif birthDay > 21 and birthDay <= 30:
            print(f'{name}, your astrological sign is Cancer.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('July'):
        print('''Which day in July where you born? Please enter only the
number for example if you where born on July 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 22:
            print(f'{name}, your astrological sign is Cancer.')
        elif birthDay > 22 and birthDay <= 31:
            print(f'{name}, your astrological sign is Leo.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('August'):
        print('''Which day in August where you born? Please enter only the
number for example if you where born on August 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 22:
            print(f'{name}, your astrological sign is Leo.')
        elif birthDay > 22 and birthDay <= 31:
            print(f'{name}, your astrological sign is Virgo.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('September'):
        print('''Which day in September where you born? Please enter only the
number for example if you where born on September 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 22:
            print(f'{name}, your astrological sign is Virgo.')
        elif birthDay > 22 and birthDay < 30:
            print(f'{name}, your astrological sign is Libra.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('October'):
        print('''Which day in October where you born? Please enter only the
number for example if you where born on October 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 24:
            print(f'{name}, your astrological sign is Libra.')
        elif birthDay > 24 and birthDay <= 31:
            print(f'{name}, your astrological sign is Scorpio.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
        
    elif birthMonth == ('November'):
        print('''Which day in November where you born? Please enter only the
number for example if you where born on November 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 23:
            print(f'{name}, your astrological sign is Scorpio.')
        elif birthDay > 23 and birthDay <= 30:
            print(f'{name}, your astrological sign is Sagittarius.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
            
            
    elif birthMonth == ('December'):
        print('''Which day in December where you born? Please enter only the
number for example if you where born on December 18 please enter only 18. ''')
        birthDay = int(input())
        if birthDay <= 21:
            print(f'{name}, your astrological sign is Sagittarius.')
        elif birthDay > 21 and birthDay <= 31:
            print(f'{name}, your astrological sign is Capricorn.')
        else:
            print(f'''Sorry {name} but there is not {birthDay} Days in
{birthMonth}.''')
        
            
    else:
        print(f'''Sorry {name} but {birthMonth} is not a month in the the Gregorian
calendar.''')

        
elif yes == ('no'):
        print(f'''Ok {name} if you ever want to know your astrological sign let me
know.''')
