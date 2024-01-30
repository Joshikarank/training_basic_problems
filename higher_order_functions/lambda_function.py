

'''
Lambda Functions are anonymous functions means that the function is without a name.
the def keyword is used to define a normal function in Python.
the lambda keyword is used to define an anonymous function in Python. 
'''


string1 = "hello"
rs = lambda i : i.upper()
print(rs(string1))

	
maxx = lambda a,b: a if( a > b ) else b
print(maxx(22,3))


minn = lambda x,y: min(x,y)
print(min(1,3))

cube = lambda p : p**3
print(cube(3))


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)

import functools
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y ), li)
print(sum)


lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


from collections import Counter 

my_list = ["joshi", "geeg", "osjhi", "practice", "aa"] 
str = "isohj"

print("hello world")



'''hi everyone'''

#comment


result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list)) 

print(result) 


def is_multiple_of_3(num):
	return num % 3 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result1 = list(filter(lambda x: is_multiple_of_3(x), numbers))
print(result1)
