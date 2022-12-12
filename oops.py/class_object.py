class car: #creating class
    attr1= 'Audi'
    attr2= "Benz"

    def names(self): #creating function
        print("the car name is",self.attr1)
        print("the car name is",self.attr2)

myCar = car() # creating an object. myCar is an Object and car is class
print(myCar.attr1)
myCar.names()    