total=0    #global variable

def sum(para1,para2):
    total= para1+para2    #local variable
    print("The total is",total)
    return total

sum(10,20)
print("new total is ",total)