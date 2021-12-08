print('Hello my name is Com Puter, what is you name?.')
name = input().capitalize()

print(f'{name} would you like to know your astrological sign?')
print('Please answer with yes or no.')
yes = input()
if yes == ('yes'):
    print('''To find your astrological sign we need to know when is your
birthday.''')
    print('''pick the number that is within the range of your birthday.
For example if you where born on March 27 pick number 1.''')
 
    print('Enter 1 if your birthday falls between March 21  – April 19')
    print('Enter 2 if your birthday falls between April 20  – May 20')
    print('Enter 3 if your birthday falls between May 21 – June 21')
    print('Enter 4 if your birthday falls between June 22 - July 22')
    print('Enter 5 if your birthday falls between July 23 - August 22')
    print('Enter 6 if your birthday falls between August 23 - September 22 ')
    print('Enter 7 if your birthday falls between September 23 - October 23 ')
    print('Enter 8 if your birthday falls between October 24 - Novermve 22 ')
    print('Enter 9 if your birthday falls between November 23 - December 21 ')
    print('Enter 10 if your birthday falls between December 22 - January 19')
    print('Enter 11 if your birthday falls between January 20 - February 18 ')
    print('Enter 12 if your birthday falls between February 19 - March 20 ')
    print('Please enter the number below here.')
    birthday = input().capitalize()
    if birthday == ('1'):
         print(f'{name} you picked number 1, your astrological sign is Aries.')
    elif birthday == ('2'):
         print(f'{name} you picked number 2, your astrological sign is Taurus.')
    elif birthday == ('3'):
         print(f'{name} you picked number 3, your astrological sign is Gemini.')     
    elif birthday == ('4'):
         print(f'{name} you picked number 4, your astrological sign is Cancer.')     
    elif birthday == ('5'):
         print(f'{name} you picked number 5, your astrological sign is Leo.')     
    elif birthday == ('6'):
         print(f'{name} you picked number 6, your astrological sign is Virgo.')     
    elif birthday == ('7'):
         print(f'{name} you picked number 7, your astrological sign is Libra.')     
    elif birthday == ('8'):
         print(f'{name} you picked number 8, your astrological sign is Scorpio')     
    elif birthday == ('9'):
         print(f'''{name} you picked number 9, your astrological sign is
Sagittarius''')     
    elif birthday == ('10'):
         print(f'''{name} you picked number 10, your astrological sign is
Capricorn''')     
    elif birthday == ('11'):
         print(f'''{name} you picked number 11, your astrological sign is
Aquarius''')     
    elif birthday == ('12'):
         print(f'{name} you picked number 12, your astrological sign is Pisces')     
    else:
        print(f'''I am sorry. You picked {birthday} taht is not a number on the
list.''')
else:
    print(f'''Ok {name} if you ever want to know your astrological sign let me
know.''')
