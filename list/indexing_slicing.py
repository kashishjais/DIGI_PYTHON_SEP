num=list(range(20))
print(num)
print('first value',num[0])
print('last value',num[-1])
num[0]=50
num[-1]=30
print(num)
print('first 3 items',num[:3])
print('last 5 items',num[-5:])
print('all items except last 2 and first 2',num[2:-2])
print(num[::-1])# reverse
print(num[::2]) # even indexes
print(num[1::2]) # odd indexes

