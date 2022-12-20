# l=[10,20,30,40,50]

# mx=max(l[0],l[1])

# sMx=min(l[0],l[1])

# n=len(1)
# for i in range(2,n):
#     if(l[i]>mx):
#         sMx=mx
#         mx=l[i]
#     elif l[i]>sMx and \
#         mx !=l[i] :    

'''
list1 = [10, 20, 4, 45, 99]
 
mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
        mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and \
        secondmax != list1[i]:
          secondmax = list1[i]
 
print("Second highest number is : ",\
      str(secondmax))
'''


l=[]
user_input=int(input("entr no of entries: "))

for i in range (1,user_input+1):
    entries=int(input("entr a num "))
    l.append(entries)

l.sort()
print("2nd largest num is ",l[-2])    