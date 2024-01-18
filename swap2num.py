'''

@Author: Joshikaran

@Date: 2024-01-18 15:40:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")
try:
    num1 = float(input("Enter the first number (a): "))
    num2 = float(input("Enter the second number (b): "))
    swap_numbers(num1, num2)
except ValueError:
    print("Please enter valid numerical values.")
