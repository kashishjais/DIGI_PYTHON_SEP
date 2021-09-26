'''we have  a continue keyword which is used to skip
a loop iteration/step'''
i=int(input("enter value of i"))
while i>0:
    if i%3==0:
        i-=1
        continue
    print(i)
    i-=1