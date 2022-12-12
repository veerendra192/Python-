
# Create a class - Employee for two employees with some objects. 
# Fetch name,age and salary and display it in the screen.


class Employee:
    company="aditya college" #this is class attribute

    def __init__(self,name,age,salary):   # default constructor
        self.name=name                    #name,age,salary are attributes   
        self.age=age
        self.salary=salary

# creating objects
emp1=Employee("sita",20,200000) 
emp2=Employee("rahul",24,200000)

print(f"{emp1.name} and {emp2.name} works in {emp1.__class__.company} ")
print(f"{emp1.name}'s age is {emp1.age} and salary is {emp1.salary}")
print(f"{emp2.name}'s age is {emp2.age} and salary is {emp2.salary}")

