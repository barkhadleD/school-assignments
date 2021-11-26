print('Hello my name is Bender, what is your name?')
Name = input().capitalize() 
print(f'''{Name} would you like to know how many days are in a specific month
of the year? Please answer with yes or no.''')
yes = input()


if yes == ('yes'):
    print(f'ok {Name} please enter a month of the year.')
    month = input().capitalize()

    if month == ('January'):
        print (f'there are 31 days in the month of {month}')
        
    elif month == ('March'):
        print (f'there are 31 days in the month of {month}')
        
    elif month == ('May'):
        print (f'there are 31 days in the month of {month}')
        
    elif month == ('July'):
        print (f'there are 31 days in the month of {month}')
        
    elif month == ('August'):
        print (f'there are 31 days in the month of {month}')
        
    elif month == ('October'):
        print (f'there are 31 days in the month of {month}')
        
    elif month == ('December'):
        print (f'there are 31 days in the month of {month}')
        
    
    elif month == ('April'):
        print(f'there are 30 days in the month of {month}')
        
    elif month == ('June'):
        print(f'there are 30 days in the month of {month}')
        
    elif month == ('September'):
        print(f'there are 30 days in the month of {month}')
        
    elif month == ('November'):
        print(f'there are 30 days in the month of {month}')

        
    elif month == ('February'):
        print (f'there are 28 days in the month of {month}')
    
print(f'Ok {Name} thank you for your time.')

