# Floxus Python Bootcamp : Assignment -1
# 3. Write a program to print the following number pyramid?

"""
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

"""

for i in range(5):
    for j in range(i+1):
        print(j+1, end = ' ')
    print()
    
    
