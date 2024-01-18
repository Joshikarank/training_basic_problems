'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

try:
    user_number = int(input("Enter a number to check if it's even or odd: "))
    check_even_odd(user_number)
except ValueError:
    print("Please enter a valid integer.")
