'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
import random

def flip_coin_percentage(num_flips):
    if num_flips <= 0:
        print("Number of flips should be a positive integer.")
        return
    heads_count = 0
    tails_count = 0
    for _ in range(num_flips):
        outcome = random.randint(0, 1)
        
        if outcome == 0:
            tails_count += 1
        else:
            heads_count += 1
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    print(f"Percentage of Heads: {heads_percentage}%")
    print(f"Percentage of Tails: {tails_percentage}%")

try:
    num_flips = int(input("Enter the number of times to flip the coin: "))
    flip_coin_percentage(num_flips)
except ValueError:
    print("Please valid integer")
