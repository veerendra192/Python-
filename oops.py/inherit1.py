class Person(object):

    def __init__(self,name,id): #parameterised constructor
        self.name=name
        self.id=id

    def display(self):
        print(self.name,self.id)

emp=Person("Aditya",21)
emp.display()

class Emp(Person):

    def Print(self):
        print("emp class called")

empDetails=Emp("mahesh",22)
empDetails.Print()
empDetails.display()      


