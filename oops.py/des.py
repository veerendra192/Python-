class Employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructor called employee deleted")  
emp= Employee()
del emp 
#emp = Employee()       