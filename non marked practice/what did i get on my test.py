#This program tells the user the persentage the get on a test and whether they
#passed or failed

print('How many marks are there on your test.')
marks = float(input())
print ('How many marks did you get in the test')
score = float(input())
percentage = (score/marks)* 100
percentage = round(percentage,1)#This rounds it

print(f'On your test you got {percentage}%')

if percentage < 50:
    print('you failed the test')

elif percentage >= 50:
    print('you passed the test')
