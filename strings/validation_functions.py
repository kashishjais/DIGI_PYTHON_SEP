value=input("enter something ")
ans=value.isupper()
print("is the value in uppercase?",ans)
ans=value.islower()
print("is value in lowercase? ",ans)
ans=value.isalpha()
print("does value has only alphabets ",ans)
ans=value.isnumeric()
print("does the value contain only numbers? ",ans)
ans=value.isspace()
print("does value has only spaces? ",ans)
ans=value.isprintable()
print("is value printable on screen? ",ans)
ans=value.isdigit()
print("does value has only digits? ",ans)

name="Dr ram"
if name.startswith("Dr"):
    print("hello doctor!")


file=input("enter file name with extension ")
if file.endswith(".exe"):
    print("executable file")
elif file.endswith(".pdf"):
    print("pdf file")    
    






