mytuple=23,56,12,11,24,67,89,90,66,65
print(mytuple.count(11))
print(mytuple.index(24))

for i in mytuple:
    print(i,end=" ")
print("reversed ")
for i in mytuple[::-1]:
    print(i,end=" ")    