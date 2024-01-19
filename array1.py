'''

@Author: Joshikaran

@Date: 2024-01-19 11:22:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-11 12:01:30

@Title : array problems in datastructure

'''


array = [23,534,123,65,11,11,11,35,567,12,44,44,44,64,1,657,1,76578,325,765,21,2,1,544,1]



'''
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
'''
def indexx():
    for i in range(len(array)):
        print(f" the index of {array[i]} in the array is {i}")



'''
2. Write a Python program to reverse the order of the items in the array.
'''
def reversed_array():
    print(array[::-1])

'''


3. Write a Python program to get the number of occurrences of a specified element in an
array.
'''
def count_occurrences(arr, element):
    return arr.count(element)

specified_ele = int(input)
occurrences = count_occurrences(array, specified_ele)



'''
4. Write a Python program to remove the first occurrence of a specified element from an
array.
'''
def remove_first_occurrence(arr, element):
    if element in arr:
        arr.remove(element)
        print(f"Removed the first occurrence of {element} from the array.")
    else:
        print(f"{element} is not present in the array.")
    
'''
getting output for each object functions
'''
indexx() #q1

reversed_array() #q2

print(f"The specified element {specified_ele} occurs {occurrences} times in the array.") #q3

print("removed array:", arrayrem.arr) #q4

specified_element = int(input("enter the first occurrence number you want to remove"))
remove_first_occurrence(array, specified_element)

print("Updated array:", array)


