'''
@Author: Joshikaran

@Date: 2024-01-20 11:42:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 12:43:30

@Title : employee wage problems 
'''

'''                                         Employee Wage Computation Problem                                                         '''



import random
import numpy

def welcome_msg():
    print("welcome to the employee wage calculator! ")




def attendance() -> int:
    """ the functions generate random numbers between range 0 to 2 , i it generates 0 then the outcome prints as absent 
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    att = random.randint(0, 2)
    if att == 0:
        print("the employee is absent...")
    else:
        print("the employee is present.")


def daily_wage() -> int:
    """sumary_line : multiplying hours and wage for full day
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    hourswage = 20
    full = 8
    wager = hourswage * full
    print(f"the wage of the  employee for full day works is : {wager}")




def part_time():
    """sumary_line adding the full hour along with the overstay hours and printing the total wager
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    hourswage = 20
    full = 8
    part_time = 8   
    overstay = part_time + full
    wager = hourswage * overstay    
    print(f"the total wager for overtime {part_time} hours along with daily wager is : {wager} ")





    
def wage_per_month():
    """calculating the monthly wager by multiplying daily wage for 20 days
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    days_per_month = 20
    hourswage = 20
    full = 8
    wager = hourswage * full
    monthly_wager = wager * days_per_month
    return monthly_wager



def wage_calculation():
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    hours_limit = random.randint(0, 100)
    days_limit = random.randint(0, 20)
    hourswage = hours_limit * 20
    wager = hourswage * days_limit 
    monthly_wager = wager * days_limit
    if hours_limit >= 100 or days_limit >= 20:
        print(f"employee had exceeded their limit , their wage is {monthly_wager}")
    else:
        print(f"the wage of the employee is {monthly_wager}")
    
    


if __name__ == "__main__":
    welcome_msg()
    attendance()
    daily_wage()
    part_time()
    wage_per_month()
    wage_calculation()