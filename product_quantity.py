

product1=int(input("product1:"))
product2=int(input("product2:"))
product3=int(input("product3:"))
# product4=int(input("product4:"))
# product5=int(input("product5:"))
'''
products =[product1,product2,product3]
for s in products:
    print(s)
'''    
344
if(product1<=0) or (product2<=0) or (product3<=0):
    print("please enter +ve value")
else:
    print("product quanity with price:")
    total=(product1*300+product2*500+product3*500)
    entries= {product1:300,product2:400,product3:500}

    x=open("productData.txt","a")
    print("the amount for total products")
    print(entries,total, file=x)

    for i,p in entries.items():
        print(i,p)
        print(i,p,file=x)
    print("the amount u need to pay is :")     
    print(total,file=x)
