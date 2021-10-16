x={1,2,3,6,8,9,0}
y={3,4,5,6}
z={11,12,34,67}
a={1,90,99,87,56}
print(x.issuperset(y))
print(y.issuperset(z))
print(z.issuperset(a))

print(x.issubset(y))
print(x.isdisjoint(y))
