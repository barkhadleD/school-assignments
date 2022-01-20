# This program is an example of using nested if statements

print ('Do you have time to answer a few questions for me?')
print ('Please answer yes or no')
question = input()

if question == ('yes'):
    print('Great')
    print()
    print('Do you like pizza?')
    print('Please answer yes or no')

    if pizza == ('yes'):
        print ('I like pizza as well.')

    if pizza == ('no'):
        print ('I like pizza as well.')

if question == ('no'):
    print("ok, thanks anyway. Have a nice day.")

print('Goodbye')
