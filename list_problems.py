'''

@Author: Joshikaran.k

@Date: 2024-01-19 14:12:24

@Last Modified by: Joshikaran.k

@Last Modified time: 2021-02-11 15:25:36

@Title : list problems in datastructure

'''

list1 = [2,5,3,1,3]

list3 = [2,1,4,5,1]

list2 = [9,8,7]


List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

'''
1. Write a Python program to sum all the items in a list.
'''

def sumlist(list1):
    print(sum(list1))
    




'''
2. Write a Python program to multiplies all the items in a list.
'''
def listprod(list1):
    res = 1
    for i in list1:
        res = i * res
    print(res)





'''
3. Write a Python program to get the smallest number from a list.
'''
def minimum(list1):
    print(min(list1))



'''
6. Write a Python program to remove duplicates from a list.
'''

def rem_duplicates(list1):
    setlist = set(list1)
    print(setlist)





'''
7. Write a Python program to clone or copy a list.
'''
def copy_list(list1):
    copy_list = list1.copy()
    print(copy_list)
    





'''
8. Write a Python program to find the list of words that are longer than n from a
given list of words.
'''

def append(list1,list2):
    list2.extend(list1)
    print(list2)





'''
15. Write a Python program to find common items from two lists.
'''
def common():
    list2.extend(list1)
    common = set(list2)
    print(common)



'''
10. Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
def remove_ele(List):
    List.pop(0)
    List.pop(4)
    List.pop(5)
    print(List)





'''
12. Write a Python program to get the difference between the two lists.
'''

def list_diff(list2,list3):
    diff=list(set(list2)-set(list3))
    print(diff)



