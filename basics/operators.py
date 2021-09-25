a=10*3 # mathematical operators
print(a)
a=10/3
print(a)
a=10//3
print(a)
a=10%3
print(a)
a=10**3
print(a)
a=10+3
print(a)
# comparison 
a=10
b=3
print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
# assignment operator
c=15
c+=10
c-=10
c*=10
print(c)
c/=10
c//=10
print(c)
c%=10
c**=10
print(c)
# logical operator
a=5
b=15
c=10
print(a>b and a>c)
print(b>a and b>c)
print(b>a or b>100)
print(not a>b)
print(a>b and a<c or b>100)

# membership- it can search a variable in an iterable
colors=['red','green','blue','yellow','purple']
print('red' in colors)
print('brown' in colors)

food=input("what would u like to eat? ")
if food in ['maggie','soup','ice cream','sandwitch']:
    print("go and cook!!")
    
