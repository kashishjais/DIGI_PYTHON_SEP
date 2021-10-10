'''when we want to create  a new list from existing list
-mapping--> create same size sequence from existing sequence
-filtering-->create  smaller sequence from existing list,using a condition'''

'''syntax
newlist=[operation loop for existing list condition]
'''
x=[22,34,555,67,89,11,33]
##mapping
x2=[i**2 for i in x]
print(x)
print(x2)

##filter
x_odd=[i for i in x if i%2!=0]
print(x_odd)
