'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def prime_factorization(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            print(i, end=' ')
    if n > 1:
        print(n)

number = int(input("Enter a number: "))
print("Prime factors:")
prime_factorization(number)