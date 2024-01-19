'''

@Author: Joshikaran.k

@Date: 2024-01-19 15:26:26

@Last Modified by: Joshikaran.k

@Last Modified time: 2021-02-11 15:26:36

@Title : tuple problems in datastructure

'''


tuple1 = (8,433,12423,'hi',74,802,4,22)

tuple2 = (1,'my name is joshikaran',6.9)

'''1. Write a Python program to create a tuple.'''
def tuples(tuple1):
    print(tuple1)




'''2. Write a Python program to create a tuple with different data types.'''

def diff_tuples(tuple2):
    print(tuple2)



'''10. Write a Python program to reverse a tuple.'''
def rev_tuple(tuple2):
    print(tuple2[::-1])



'''9. Write a Python program to slice a tuple.'''

def slice_tuple(tuple1):
    print(tuple1[:4])
    print(tuple1[4:])





'''8. Write a Python program to remove an item from a tuple.'''
def rem_item(tuple1):
    tuplea = list(tuple1)
    tuplea.remove('hi')
    tuplea.pop(5)
    print(tuplea)





'''7. Write a Python program to convert a list to a tuple.'''

sample_list = [76,234,14,'hii',368]

def conv(sample_list):
    converted = tuple(sample_list)
    print(converted)


'''6. Write a Python program to check whether an element exists within a tuple.'''
def checking(tuple1):
    inputt = int(input("enter the number you want to check: "))
    if inputt in tuple1:
        print(f"present ")
    else:
        print("not present")

