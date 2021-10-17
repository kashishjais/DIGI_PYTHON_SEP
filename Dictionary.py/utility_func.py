marks={
    'rohan':10,
    "sohan":7,
    'mohan':5,
    'rehan':9,
    'alex':6
}
print(marks.keys())

print(marks.values())

print(marks.items())

a="ramu"
b="shamu"
c="riya"
d="siya"
e="ritu"
def_marks='N/A'
new_stud=dict.fromkeys([a,b,c,d,e],def_marks)
print(new_stud)

pos=list(range(1,11))
pos_dict=dict.fromkeys(pos,"available")
print(pos_dict)

copy_of_dict=pos_dict.copy()
print(copy_of_dict)
