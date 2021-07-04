# Floxus Python Bootcamp : Assignment -1
# 10. Write a program to print Binary representation of a given number N.

n = int(input('Enter a number to get its binary: '))
i = 1 << 20
while i > 0:
    if n & i != 0:
        print('1', end='')
    else:
        print('0', end='')
    i = i // 2
    
    
