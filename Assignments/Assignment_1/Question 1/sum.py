num1 = int(input("enter num1 : "))      #taking 5 inputs from user
num2 = int(input("enter num2 : "))
num3 = int(input("enter num3 : "))
num4 = int(input("enter num4 : "))
num5 = int(input("enter num5 : "))
sum = (num1+num2+num3+num4+num5)
if(num1<=0) or (num2<=0) or (num3<=0) or (num4<=0) or (num5<=0): #checking input nums less than o requal to zero
     print("please enter +ve number") 
else:
    x=open("outputData.txt",'a')  #file handling
    print("sum of five nums:",sum)
    print("sum of five nums:",sum,file=x)
