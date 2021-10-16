stddict={'name':'billu',
        'maths':15,
        'english':18,
        'science':17,
        'hindi':19,
        'age':18,
        'study':False}

for i in stddict:
    print(i,end=" ")# for keys only

for i in stddict:
    print(stddict[i],end=" ")# for values only

for i in stddict:
    print(i,stddict[i],end=" ")# for keys and values both

for k,v in stddict.items():
    print(k,"-->",v,end=" ")# for keys and values both

