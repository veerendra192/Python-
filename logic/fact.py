num = int(input("Enter a num: "))

fact=1 #global var

if(num<0):
    print("-ve num not accepted")
elif(num==0):
    print("the fact of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("the fact of ",num, "is ",fact)           