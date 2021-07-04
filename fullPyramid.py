# Floxus Python Bootcamp : Assignment -1
# 5.Write a program to print the full pyramid?
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

for i in range(1, 6):
    for j in range(6-i):
        print(" ", end="")
        
    for j in range(i):
        print("*", end=" ")
        
    print()
