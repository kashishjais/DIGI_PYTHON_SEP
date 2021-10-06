# wap to find the sum of all elements in a list
total=0
x=[23,56,78,90,10]
for i in x:
    total+=i
print(f'total is {total}')

total=sum(x)
print(total)    
x_max=max(x)
x_min=min(x)
print(x_max)
print(x_min)
avg=sum(x)/len(x)
print(f'average is {avg}')
