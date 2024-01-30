# sample higher order functions
def caps(text):
    return text.upper()
def low(text):
    return text.lower()
print(caps("hellow wor;d"))
print(low("HELLOWORLD"))


def divisor(x):
    def divident(y):
        return x/y
    return divident
divide= divisor(10)
print(divide(2))



# Decorator functions
def sample(function1):
    def display():
        print("this comes  from the outer function")
        function1()
        print("this  also comes from the outer function")
    return display()
def btween():
    print("this comes between")
disp = sample(btween)

def sample2(function1):
    def display2():
        print("this comes  from the outer function")
        function1()
        print("this  also comes from the outer function")
    return display2()
@sample2
def btween2():
    print("this comes between")
