'''

@Author: Joshikaran

@Date: 2024-01-18 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 18:00:30

@Title : Coupon number - random 

'''
def check_vowel_consonant(alphabet):
    alphabet = alphabet.lower()

    if len(alphabet) == 1 and alphabet.isalpha():
        if alphabet in ['a', 'e', 'i', 'o', 'u']:
            print(f"{alphabet} is a vowel.")
        else:
            print(f"{alphabet} is a consonant.")
    else:
        print("alphabet .")

user_input = input("Enter an alphabet to check if it's a vowel or consonant: ")
check_vowel_consonant(user_input)
