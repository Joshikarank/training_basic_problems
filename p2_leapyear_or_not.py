'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
years = input("enter the year: ")

if len(years) != 4:
    print("Invalid Year")
else:
    years = int(years)
    if years%4 == 0:
        print("leap year")
    else:
        print("not leap")
