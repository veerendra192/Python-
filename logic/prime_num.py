user=int(input("enter a num: "))
flag=False
if(user>1):
    for i in range(2,user):
        if(user%i==0):
            flag=True
            break
if (flag):
    print(user, "is not a prime num")
else:
    print(user,"is a prime number")            

