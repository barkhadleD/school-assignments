print ('Pick the number that is beside your favourite colour.')
print ('1. Red')
print ('2. Blue')
print ('3. Greeen')
print ('4. Orange')
print ('5. Purple')
print ('6. Yellow')
print ('7. Black')
print ('8. Gold')
print()

number = input ('Please enter the number here: ')
if number == ('1'):
    print ('The colour you picked was red.')
elif number == ('2'):
    print ('The colour you picked was blue.')
elif number == ('3'):
    print ('The colour you picked was greeen')
elif number == ('4'):
    print ('The colour you picked was orange')
elif number == ('5'):
    print ('The colour you picked was purple')
elif number == ('6'):
    print ('The colour you picked was yellow')
elif number == ('7'):
    print ('The colour you picked was black')
elif number == ('8'):
    print ('The colour you picked was gold')
else:
    print(f'I am sorry. You picked {number} taht is not a valid number.')
