# Floxus Python Bootcamp : Assignment -1
# 4.Write a program to print the inverted pyramid?
"""
    * * * * *
    * * * *
    * * *
    * *
    *
"""

for i in range(5, 0, -1):
    for j in range(0 , i):
        print('* ', end='')
    print()
