'''when we want to create  a new list from existing list
-mapping--> create same size sequence from existing sequence
-filtering-->create  smaller sequence from existing list,using a condition'''

#without comprehension
x=[1,2,3,5,7,8]
x2=[]
for i in x:
    sqr=i**2
    x2.append(sqr)
print(x)    
print(x2)

x=[1,2,3,5,7,8]
x2=[]
for i in x:
    sqr=i**3
    x2.append(sqr)
print(x)    
print(x2)


#filter without compprehension
x_even=[]
for i in x:
    if i%2==0:
        x_even.append(i)
print(x)
print(x_even)
        

