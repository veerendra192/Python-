# Create a class - Student. Use the method concept, 
# to fetch student name and marks for them

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

     #method 1
    def getDetails(self):
        print(f"Hi.! My name is {self.name}, I recived {self.marks} marks")
    
    #method2 to fetch
    def getDetails(self):
        print(f"Hi..! my name is {self.name}, I revevied {self.marks} marks")

student1=Student("Rahul",90)
student2= Student("sita",78)     

student1.getDetails()
student2.getDetails()