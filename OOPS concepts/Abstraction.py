'''

@Author: Joshikaran

@Date: 2024-01-27 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-27 18:00:30

@Title : Abstraction in  OOPS 

'''

from abc import ABC , abstractclassmethod

class Norms():
    def mileage(self):
        pass
    
    @abstractclassmethod
    def emission(self):
        pass

class Car1(Norms):
    def emission(self):
        print("car1 Norms has been approved!")

class Car2(Norms):
    def emission(self):
        print("car 2 norms has been approved!")

    def mileage(self):
        print("mileage of car2 is 24 kmpL")


c1 = Car1()
c2 = Car2()

if __name__ == '__main__':
    c1.emission() # it will raise an error because its not implemented in the base
    c2.mileage()   # calling method which is defined only in child class
    