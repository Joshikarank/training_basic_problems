'''

@Author: Joshikaran

@Date: 2024-01-27 18:00:30

@Last Modified by: Joshikaran

@Last Modified time: 2021-02-27 18:00:30

@Title : Abstraction in  OOPS 

'''

class Person(object):

	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


a = Employee('Rahul', 886012, 200000, "Intern")


a.display()
a.details()
