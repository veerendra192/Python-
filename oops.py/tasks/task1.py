# Create a class - Employee for two employees with some objects. 
# Fetch name,age and salary and display it in the screen.

'''using inheritance '''

class Employee(object):

        def __init__(self, name, age, salary):
            self.name=name
            self.age=age
            self.salary=salary
        
        def displayDetails(self):
            print("Name:", self.name, ", age:", self.age, ", Salary:", self.salary)
e1=Employee("Rahul", 23, 90000)
e2=Employee("Mohan", 32, 50000)

print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
