entries=int(input("enter the entries: "))
n1,n2,=0,1

count=0
if(entries<=0):
    print("enter +ve num")
elif(entries==1):
    print("fabino upto",entries)
    print(n1)
else:
    print('fibinoseries ')
    while(count<entries):
        print(n1)
        nth=n1+n2
        n1-n2
        n2-nth
        count+=1
        

