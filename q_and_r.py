'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def compute_quotient_and_remainder(dividend, divisor):
    if divisor == 0:
        print("Error: Division by zero is undefined.")
        return None
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    
    result = compute_quotient_and_remainder(dividend, divisor)
    if result is not None:
        quotient, remainder = result
        print(f"Quotient: {quotient}")
        print(f"Remainder: {remainder}")
except ValueError:
    print("Please enter valid integers for dividend and divisor.")
