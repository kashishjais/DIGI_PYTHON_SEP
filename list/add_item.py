x=[] ## empty list
print("enter 3 values")
for i in range(3):
    val=input('->')
    x.append(val)
print(x)
x.append(10)
x.append([1,3,2])
x.append(True)
x.append("hello")
print(x)

x.insert(0,99)
x.insert(2,55)
print(x)

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
print(b)
b.extend(a)
print(b)