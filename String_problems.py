'''
@Author: Joshikaran.k

@Date: 2024-01-20  10:14:29

@Last Modified by: Joshikaran.k

@Last Modified time: 2024-01-20 10:15:36

@Title : string problems in datastructure
'''


string1 = "Hello im JK"


'''1. Write a Python program to calculate the length of a string.'''
def length_strings(string1):
    return(len(string1))






'''2. Write a Python program to count the number of characters (character frequency) in a
string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''

def charf(string1):
    dict1={}
    for i in string1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
            return(dict1)
        






'''3. Write a Python program to get a string from a given string where all occurrences of its
first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

def string_(string1):
    if len(string1)==0:
        return('')
    elif string1[0]!=string1[1]:
        return(string1[0]+'$'+string_(string1[1:]))
    
                     





'''4. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

def ing_ly(string1):
    if len(string1) < 3:
        return string1
    elif 'ing' in string1:
        return string1 + 'ly'
    else:
        return string1 + 'ing'







'''5. Write a Python function that takes a list of words and returns the length of the longest
one.
'''
test_list = ['gfg', 'is', 'best', 'for', 'geeks', 'aaaaaa']

def print_long(test_list):
    maximum = max(test_list , key = len)
    return maximum 







'''11. Write a Python program to reverse a string.'''

def rev(string1):
    return string1[::-1]






'''12. Write a Python program to lowercase first n characters in a string'''

def lower_first(string1):
    return (string1[0].lower()+string1[1:])





'''6. Write a Python script that takes input from the user and displays that input back in
upper and lower cases.'''

def lowerandup():
    inputstr = input("input your string: ")
    print(f"the lowercase of the strings is: {inputstr.lower()} , the uppercase is : {inputstr.upper()} ...")





