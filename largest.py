'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def find_largest_number(num1, num2, num3):
    largest_number = max(num1, num2, num3)
    print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    find_largest_number(number1, number2, number3)
except ValueError:
    print("Please enter valid numerical values.")
