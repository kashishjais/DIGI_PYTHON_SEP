'''wap to ask the user his/her expenses on different items.take  around 15 items and then find sum and average
on the values'''
s=0
dict={}
for i in range(15):
    k=input("enter key ")
    v=int(input("enter value "))
    dict[k]=v 
    s+=v
print(dict)
print("sum:",s)
print("avg:",s/15)


