# wap to create a user input list
# user should decide the size of list
# display list values ,min , max ,mean ,average
# list should be numeric
x=[] 
size=int(input("enter size of list"))
for i in range(size+1):
    ele=int(input("enter element"))
    x.append(ele)
print(x)
print(max(x))
print(min(x))
print('total is', sum(x))
print('average is',sum(x)/len(x))
   