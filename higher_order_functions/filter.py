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

