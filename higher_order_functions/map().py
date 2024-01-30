'''The map() function applies a given function to 
all items in an input iterable (e.g., list) 
and returns an iterator that produces the results.'''

number_list = [2,5,8,2,9]

squares = list(map(lambda x : x**2 , number_list))
cube = list(map(lambda x : x**3 , number_list))
print(squares)
print(cube)


#map can also used to take multiple inputs in single line
x,y,z = map(int ,input("enter 3 numbers: ").split())
print(f"the input numbers are {x,y,z}")
print(f"ther sum is : {x+y+z}")

#sum of 2 lists using map
list1 = [2,7,3,88]
list2 = [33,53,23,1]
sumslist = list(map(lambda a,b : a + b,list1 , list2))
print(sumslist)

