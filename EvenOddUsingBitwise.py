#Floxus Python Bootcamp : Assignment - 1
#1. Write a program to check a number is even or odd using bitwise operator?

number = int(input("Enter a number:"))
if number ^ 1 == number + 1:
    print('Even')
else:
    print('Odd')
