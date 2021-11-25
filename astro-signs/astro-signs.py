print('Hello my name is Com Puter, what is you name?.')
Name = input().capitalize()

print(f'{Name} would you like to know your astrological sign?')
print('Please answer with yes or no.')
Yes = input()
if Yes == ('yes'):
    print('To find your astrological sign we need to know your what is your birthday.')
    print('''pick the number that is within the range of your birthday.
          For example if you where born on March 27 pick number 1.''')
 
    print('Pick 1 if your birthday falls between March 21  – April 19')
    print('Pick 2 if your birthday falls between April 20  – May 20')
    print('Pick 3 if your birthday falls between May 21 – June 21')
    print('Pick 4 if your birthday falls between June 22 - July 22')
    print('Pick 5 if your birthday falls between July 23 - August 22')
    print('Pick 6 if your birthday falls between August 23 - September 22 ')
    print('Pick 7 if your birthday falls between September 23 - October 23 ')
    print('Pick 8 if your birthday falls between October 24 - Novermve 22 ')
    print('Pick 9 if your birthday falls between November 23 - December 21 ')
    print('Pick 10 if your birthday falls between December 22 - January 19')
    print('Pick 11 if your birthday falls between January 20 - February 18 ')
    print('Pick 12 if your birthday falls between February 19 - March 20 ')
        Birthday = input().capitalize()
    if Birthday == ('1'):
         print(f'{Name} Your astrological sign is Aries')
    elif Birthday == ('2'):
         print(f'{Name} Your astrological sign is Taurus')
    elif Birthday == ('3'):
         print(f'{Name} Your astrological sign is Gemini')     
    elif Birthday == ('4'):
         print(f'{Name} Your astrological sign is Cancer')     
    elif Birthday == ('5'):
         print(f'{Name} Your astrological sign is Leo')     
    elif Birthday == ('6'):
         print(f'{Name} Your astrological sign is Virgo')     
    elif Birthday == ('7'):
         print(f'{Name} Your astrological sign is Libra')     
    elif Birthday == ('8'):
         print(f'{Name} Your astrological sign is Scorpio')     
    elif Birthday == ('9'):
         print(f'{Name} Your astrological sign is Sagittarius')     
    elif Birthday == ('10'):
         print(f'{Name} Your astrological sign is Capricorn')     
    elif Birthday == ('11'):
         print(f'{Name} Your astrological sign is Aquarius')     
    elif Birthday == ('12'):
         print(f'{Name} Your astrological sign is Pisces')     

    
else:
    print(f'Ok {Name} if you ever want to know your astrological sign let me know.')
