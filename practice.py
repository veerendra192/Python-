'''
n =10
if (n<=0):
    print("n is less than zero")
elif (n<=5):
    print("n is less than or eqaul to 5")
else:
    print("n is = to or higher than 10") '''      

#for loop
'''
students =['sandeep','rahul','kkk', 'lub','ravee']
print("student names are:")
for i in students:
    print(i)
'''

list=[1,2,3.5,4.5,'aditya',True]
'''
print(list[4])
print(list[1:3]) #include 1 index include & excluded index 3
print(list[1:5])
print(list[2:])
print(list*2)
'''

list2=['sandeep','mohan']
'''
print(list+list2)
print(list2+list)
'''

t=(1,2,3.5,4.5,'aditya', True)
'''
print(t[0])
print(t[1:4])
print(t[2:])
'''

details = {'ram':90, 'rahul':80, 'satya':50, 'anik':100}
details[4]="Test"
# print(details)
# print(details.values())
# print(details.keys())
# print(details[4])
# print(details)
'''
college=input()
location=input()
stream=input()
dict = {
    'college':"aditya",
    'loaction':"ap",
    'stream': "ME"
}
for info in dict:
    print(info)
for info_1 in dict:
    print(dict[info_1])    
'''
# dict_1 ={}
# for i in range(3):
#     college=input()
#     loaction=input()
#     stream = input()
# college ={}
name =input("ent the name:")
roll = input("ent the roll:")
college = {name:roll}
print(college)  
