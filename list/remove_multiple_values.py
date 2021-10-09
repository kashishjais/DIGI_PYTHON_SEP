x=[2344,1,1,2,2,2,3,3,3,
222,444,33,11,222,333,5,
6,6,456,789,987,1111]
x.count(3)
for i in range(x.count(3)):
    x.remove(3)
print(x)    
 
 # or 
y=x.copy()
while 3 in y:
    idx=y.count(3)
    y.pop(idx)
print(y)    
