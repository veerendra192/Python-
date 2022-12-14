#print even avg btw range of min MAX
min = int(input(" Please Enter the minimum Value : "))
max=int(input(" Please Enter the Maximum Value : "))
sumOfEven=0

for number in range(min,max+1):
    if(number % 2 == 0):
        sumOfEven+=1
print("avg of even nums between range",sumOfEven)
