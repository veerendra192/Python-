class Person(object):
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):

    def isEmployee(self):
        return True

Emp=Person("anik")
print(Emp.getName(),Emp.isEmployee())

Emp1=Employee("Sachin")
print(Emp1.getName(),Emp1.isEmployee())
