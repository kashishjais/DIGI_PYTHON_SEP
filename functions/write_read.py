def combine():
    data=''
    while True:
        line=input("->")
        if line:
            data+=line+'\n'
        else:
            break
    return data

def write_show(filename):
    print("enter some data ")
    data=combine()
    file=open(filename,'w+')
    file.write(data)
    file.seek(0)
    content=file.read()
    file.close()
    print(content)

write_show("kiya.txt")
    