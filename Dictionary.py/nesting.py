class_9={
    'teacher':'AB sir',
    'student':{
        '001':{
            'name':'raaj',
            'father_name':'Mr abc',
            'grade':'A'
        },
        '002':{
            'name':'ritu',
            'father_name':'Mr singh',
            'grade':'B'
    },
    '009':{
            'name':'ram',
            'father_name':'Mr Sharma',
            'grade':'A'
}
    }
}
print(class_9)

from pprint import pprint
pprint(class_9)

print(class_9['student']['002']['father_name'])
print(class_9['student']['009']['grade'])

print(class_9['student']['001']['name'])


##loop
for k,val  in class_9.items():
    print(k,end="->")
    if isinstance(val,str):
        print(val)
    if isinstance(val,dict):
        for k,data in val.items():
            print(k,end="->")
            if issubclass(data,str):
                print(data)
            if isinstance(data,dict):
                for k,v in data.items():
                    print(k,end="->")
                    if isinstance(v,str):
                        print(v)        