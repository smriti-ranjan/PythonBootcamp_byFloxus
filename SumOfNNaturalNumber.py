# Floxus Python Bootcamp : Assignment -1
# 7.Write a program to find the sum of first N natural number using for loop?

N = 10
sum = 0

for i in range(1, N+1):
    sum = sum + i
    i += 1
print(f'Sum of first {N} natural numbers: {sum}')
