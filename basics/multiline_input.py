all_data=''#blank string
while True:
    line=input("~")
    if not line:
        break
    all_data+=line

print(all_data)    
print('you wrote',len(all_data),'chars')


