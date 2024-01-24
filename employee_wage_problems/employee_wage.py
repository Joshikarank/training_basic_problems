'''

@Author: joshikaran

@Date: 2024-01-20 11:30:00

@Last Modified by: joshikaran

@Last Modified time: 2024-01-20 11:30:00

@Title : Creating Employee Wage Program

'''
import random

        
class Employee:
    def _init_(self,name,wage_per_hour,full_day_hour,part_time_hour,no_of_days,no_of_hours):
        self.name=name
        self.wage_per_hour=wage_per_hour
        self.full_day_hour=full_day_hour
        self.part_time_hour=part_time_hour
        self.no_of_days=no_of_days
        self.no_of_hours=no_of_hours
        self.days=0
        self.hours=0
        self. wage=0
    
    @staticmethod
    def check_attendance():
        attendance_type=random.randint(0,2)
        return attendance_type
    
    def caluclate_daily_wage(self):
        self.attendance=self.check_attendance()
        match self.attendance:
            case 2:
                return self.full_day_hour
            case 1:
                return self.part_time_hour
            case 0:
                return 0
            
    def calculate_monthly_wage(self):
        
        while self.days<self.no_of_days and self.hours<self.no_of_hours:
            self.days += 1
            self.hours+=self.caluclate_daily_wage()
            
        self.wage = self.hours * self.wage_per_hour
        return self.hours,self.wage,self.days
            

class Company:
    def _init_(self,company_name):
        self.company_name=company_name
        self.emplyoee_dict={}

    def add(self,emp):
        if emp.name not in self.emplyoee_dict:
            self.emplyoee_dict[emp.name]=emp

    def display(self,employee_name):
        if employee_name in self.emplyoee_dict:
           emp=self.emplyoee_dict[employee_name]
           print(f"{emp.name} worked for {emp.days} days {emp.hours} hours his monthly wage is {emp.wage}")
        else:
            print("Employee not found")
    
    def update(self,employee_name,wage_per_hour):
        if employee_name in self.emplyoee_dict:
            self.emplyoee_dict[employee_name].wage_per_hour=wage_per_hour
            self.emplyoee_dict[employee_name].calculate_monthly_wage()

        

    def delete(self,employee_name):
        if employee_name in self.emplyoee_dict:
            del self.emplyoee_dict[employee_name]
        else:
            print("Employee not found")
    

class MultipleCompanies:
    def _init_(self):
        self.companies={}

    def add_company(self,company):
        if company.company_name not in self.companies:
            self.companies[company.company_name]=company

    def get_company(self,company_name):
        if company_name in self.companies:
            return self.companies[company_name]
        else:
            print("The company not found")
        
    def delete_company(self,company_name):
        if company_name in self.companies:
            del self.companies[company_name]

    


def main():
    print("Welcome to Employee Wage problem")
    MultipleCompanies=MultipleCompanies()
    company = Company('ABC')
    while True:
        choice = int(input('Enter 1 to add, 2 to update, 3 to display, 4 to delete : '))
        if choice == 1:
            employee_name=input("Enter the employee_name: ")
            wage_per_hour=int(input("Enter the wage_per_hour: "))
            full_day_hour=int(input("Enter the full_day_hour: "))
            part_time_hour=int(input("Enter the part_time_hour: "))
            no_of_days=int(input("Enter the no_of_days: "))
            no_of_hours=int(input("Enter the no_of_hours: "))
            employee = Employee(employee_name,wage_per_hour,full_day_hour,part_time_hour,no_of_days,no_of_hours)
            employee.calculate_monthly_wage()
            company.add(employee)
        elif choice==2:
            employee_name=input("Enter the employee_name: ")
            new_wage=input("Enter the new wage_per_hour: ")
            company.update(employee_name,new_wage)
        elif choice ==3:
            employee_name=input("Enter the employee_name: ")
            company.display(employee_name)
        elif choice==4:
            employee_name=input("Enter the employee_name: ")
            company.delete(employee_name)
        else:
            break



if __name__=="__main__":
    main()