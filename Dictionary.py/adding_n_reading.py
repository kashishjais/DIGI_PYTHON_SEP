words={}
words['alpha']='number one,starting value,or the top value'
print("user input-->")
for i in range(3):
    k=input("enter a word ")
    v=input("enter the meaning ")
    words[k]=v
print(words)    
print(words["alpha"])
print(words.get('alpha'))
print(words.get('beta','not found'))