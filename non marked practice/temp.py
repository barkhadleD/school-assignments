#5 degrees celsius or colder wear winter coat
#In between 6 and 18 degrees celsius wear a sweater
#Any thing higher then 18 degrees celsius they will wear a shorts and a t-shirt

print('What is the tempreture outside? Only write a numbers. For example 3.')
temp = int(input())

if temp <= 5:
    print('Wear a winter coat.')
elif temp >= 6 and temp <= 18:
    print('Wear a sweater.')
elif temp > 18:
    print('Wear shorts and a t-shirt.')
