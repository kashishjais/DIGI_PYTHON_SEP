num=list(range(5,15))
for ele in num:
    print(ele)
words=["this","that","who","whom"]
for item in words:
    print(len(item))    

coords=[[1,2],[2,3],[5,6]]
for i in coords:
    print(i)    
for i in coords:
    print(i[0],i[1]) 

for  idx,val in enumerate(words):
    print(f'{idx} has {val}')

for i in num:
    if i%3==0:
        print(i) 
           

