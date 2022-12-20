import pandas as pd  #imoprting pandas
l=[]
for i in range(5): 
    value= int(input("enter a value: "))  #taking 5 inputs using for loop
    l.append(value**2)     #appending                         
powerOfValue= pd.Series(l)
print(powerOfValue)   #printing