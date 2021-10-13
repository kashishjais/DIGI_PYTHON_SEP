x={1,2,3,4,6}
y={4,8,9,0,4,5}
common=x.intersection(y)
print("x and y have ",common)
xuniq=x.difference(y)
yuniq=y.difference(x)
print(xuniq)
print(yuniq)

# not to be used in code actually
x.intersection_update(y)

