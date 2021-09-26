'''break keyword is used to terminate a loop'''
name=input("what is ur name?")
size= len(name)
while size>0:
    size-=1
    if name[size]==" ":
        print("space  has been found in name")
        break
    else:
        print(name[size],end=" ")    
