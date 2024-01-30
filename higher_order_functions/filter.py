'''he filter() function in Python is another built-in function that is used to construct an iterator 
from elements of an iterable for which a function returns true. In other words,
 it filters the elements of an iterable based on a specified condition. The syntax of the filter() function is as follows:
filter(function, iterable)'''


def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):	
		return True
	else:
		return False
	
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)
	


seq = [0, 1, 2, 3, 5, 8, 13]

result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

