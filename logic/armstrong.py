num = int(input("enter a num : "))
sum =0

temp=num
while(temp>0):
    digit=temp %10
    # print(digit)
    sum+=digit**3
    # print(sum)
    temp //=10
    # print(temp)

if(num==sum):
    print(num,"is armstrong")
else:
    print(num,"is not a armstrong")    


