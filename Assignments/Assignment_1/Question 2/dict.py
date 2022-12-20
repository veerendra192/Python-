Car = {} # creating dict

req = int(input("no of cars info required: "))  #taking input   
for i in range(req):
    brand = input("Car brand name: ")
    carColour = input("Car colour: ")
    Car[brand] = carColour
    x = open("outputData.txt", "a") #file handling
    print("cars info",Car)
    print("cars info: ",Car, file=x)  