'''wap to create a dict that contains following sequence
1:1
2:4
3:9
....
....
100:10000'''
'''wap to sort the dict of 5 elements
you can put anything inside the dict'''

dict={}
for i in range(101):
    k=i
    v=i*i
    dict[k]=v 
print(dict)

dict2={'R':'red','B':'blue','Y':'yellow','G':'green','W':'white'}
    
print(sorted(dict2.items()))
