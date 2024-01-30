a =500
b = "ffbger"


try:
    print(a/b)
#defining the data type error 
except TypeError:
    print("cannot add strings and int")


c = 0
#defining for all type of errors
try:
    print(a/c)
except:
    print("cant div by 0")


#specifically for division by zero error
try:
    print(a/c)
except ZeroDivisionError:
    print("cannot divide by zero (from using specific type of error)")


'''the finally keyword make the bloxk of code always 
execute under it if or not errors have been found'''
try:
    print(a/c)
except ZeroDivisionError:
    print("this is a zero division error ")
finally:
    print("Fix the errors")

#still finally block will be executed even it has no errors
try:
    print(a/a)
except ZeroDivisionError:
    print("this is a zero division error now the finally block is going to be executed")
finally:
    print("Code execution has end!")


try: 
	raise NameError("Hi there")
except NameError:
	print ("An exception")
	raise

def example_function(x):
    if o < 0:
        raise ValueError("Input must be a non-negative number")
    return o ** 2

try:
    result = example_function(-5)
except ValueError as ve:
    print(f"Error: {ve}")
# Output: Error: Input must be a non-negative number


