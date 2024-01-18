'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def prime_factorization(n):
    print(f"Prime factors of {n} are:")

    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            print(i, end=" ")
            n = n // i

    if n > 2:
        print(n)

try:
    N = int(input("Enter a number to find its prime factors: "))
    prime_factorization(N)
except ValueError:
    print("Please enter a valid integer.")
