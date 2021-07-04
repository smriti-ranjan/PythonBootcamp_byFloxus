# Floxus Python Bootcamp : Assignment -1
# 9. Write a program to check whether a number is prime or not?

number = int(input('Enter a number to check if prime: '))

i = 2
if number <= 0:
    print('Invalid Input!!')
elif number == i:
    print('Prime')
elif number % i == 0 or number == 1:
    print('Not prime')
else:
    print('Prime')
