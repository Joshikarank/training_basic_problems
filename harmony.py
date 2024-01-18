'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def harmonic_number(n):
    if n == 0:
        print("N should be greater than 0.")
        return

    result = 0.0
    for i in range(1, n + 1):
        result += 1 / i

    print(f"The {n}th Harmonic Value is: {result}")
try:
    N = int(input("Enter the value of N: "))
    harmonic_number(N)
except ValueError:
    print("Please enter a valid integer for N.")
