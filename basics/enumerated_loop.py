msg="we will be victorious"
for i in enumerate(msg):
    print(i)

for i,c in enumerate(msg):
    if i%2!=0:
        print(c,end=" ")
    
num=[12,3,56,76,43] 
num2=[23,56,87,90,12]
for i,j in zip(num,num2):
    print(i,j)  

for i,j in zip(num,num2):
    print(i+j)
    
