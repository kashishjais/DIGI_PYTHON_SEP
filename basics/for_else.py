'''for else is a special variation for for loop where we can check 
if the for loop completed  all the iterations or not,else block will only execute if 
all steps are completed'''
#prime no.
num=int(input("enter the number"))
for i in range(2,num):
    if num%i==0:
        print("non prime")
        break
else:
    print("prime no.")

