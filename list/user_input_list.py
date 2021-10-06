# wap to create a user input list
# user should decide the size of list
# display list values ,min , max ,mean ,average
# list should be numeric
x=[] 
t=0
size=int(input("enter size of list"))
for i in range(size+1):
    ele=int(input("enter element"))
    x.append(ele)
    t+=ele
print(x)
avg=t/size
x_max=max(x)
x_min=min(x)
print(f'total is {t}')
print(f'average is {avg}')
print(x_max)
print(x_min)    