# Floxus Python Bootcamp : Assignment -1
# 6. Write a program to print Floyds Triangle?
"""
    1
    2 3
    4 5 6
    7 8 9 10
"""
x = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(x, '', end='')
        x += 1
    print()
