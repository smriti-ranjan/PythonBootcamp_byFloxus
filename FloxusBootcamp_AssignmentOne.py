#!/usr/bin/env python
# coding: utf-8

# #                                       Floxus Python Bootcamp : Assignment - 1
# 
# 1. Write a program to check a number is even or odd using bitwise operator?
# 2. Write a program to calculate 2^x using bitwise operator?
# 3. Write a program to print the following number pyramid?
# 
#     ```
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
# 
#     ```
# 
# 4. Write a program to print the inverted pyramid?
# 
#     ```
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *
# 
#     ```
# 
# 5. Write a program to print the full pyramid?
# 
#     ```
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
# 
#     ```
# 
# 6. Write a program to print Floyds Triangle?
# 
#     ```
#     1
#     2 3
#     4 5 6
#     7 8 9 10
#     ```
# 
# 7. Write a program to find the sum of first N natural number using for loop?
# 8. Write a program to print all the digits of a number?
# 
#     ```
#     SAMPLE INPUT 
#     321
#     486
# 
#     SAMPLE OUTPUT
#     3  2  1
#     4  8  6
# 
#     ```
# 
# 9. Write a program to check whether a number is prime or not?
# 10. Write a program to print Binary representation of a given number N.

# ### 1. Write a program to check a number is even or odd using bitwise operator?

# In[14]:


number = int(input("Enter a number:"))
if number ^ 1 == number + 1:
    print('Even')
else:
    print('Odd')


# ### 2. Write a program to calculate 2^x using bitwise operator?

# In[15]:


x = int(input('Enter the value of x: '))
print(f'Result of 2^x is {2^x}')


# ### 3. Write a program to print the following number pyramid?
# 
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5

# In[16]:


for i in range(5):
    for j in range(i+1):
        print(j+1, end = ' ')
    print()


# ### 4.Write a program to print the inverted pyramid?
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

# In[17]:


for i in range(5, 0, -1):
    for j in range(0 , i):
        print('* ', end='')
    print()


# ### 5.Write a program to print the full pyramid?
#             *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
# 

# In[18]:


for i in range(1, 6):
    for j in range(6-i):
        print(" ", end="")
        
    for j in range(i):
        print("*", end=" ")
        
    print()


# ### 6. Write a program to print Floyds Triangle?
#     1
#     2 3
#     4 5 6
#     7 8 9 10

# In[19]:


x = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(x, '', end='')
        x += 1
    print()


# ### 7.Write a program to find the sum of first N natural number using for loop?

# In[20]:


N = 10
sum = 0

for i in range(1, N+1):
    sum = sum + i
    i += 1
print(f'Sum of first {N} natural numbers: {sum}')


# ### 8. Write a program to print all the digits of a number?
# 
#     SAMPLE INPUT
#     321
#     486
# 
#     SAMPLE OUTPUT
#     3  2  1
#     4  8  6
# 

# In[11]:


n = input('Enter a number: ')
for x in str(n):
    print(x, '', end='')
    


# ### 9. Write a program to check whether a number is prime or not?

# In[22]:


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


# ### 10. Write a program to print Binary representation of a given number N.

# In[23]:


n = int(input('Enter a number to get its binary: '))
i = 1 << 20
while i > 0:
    if n & i != 0:
        print('1', end='')
    else:
        print('0', end='')
    i = i // 2


# ______________________________________________________________________________________________________________________________
# 
# #### Assignment Posted : Thursday - July 1, 2021
# #### Submission Deadline : Saturday - July 3, 2021
# 
# #### Submitted by: `Smriti Ranjan`
# #### Email id : `smritiranjan17@gmail.com`
# 
