'''

@Author: Joshikaran

@Date: 2024-01-27 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-27 18:00:30

@Title : Abstraction in  OOPS 

'''

class parent():
    def display(self):
        print("I am the parent method")

class child1(parent):
    def disp(self):
        print("this is a child class 1")

class child2(parent):
    def display1(self):
        print("this is a child class 2")

Child1 = child1()
Child2 = child2()

if __name__ == '__main__':
    Child2.display()
    Child1.disp()



