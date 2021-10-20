''' file handling basics 
1.read file -open()
2.write file -open()
3. update file- open()
open() funtion sets the mode of file,it returns file object'''


file=open('dummy.txt')
print(file.read())
file.close()

f1=open('radiants.txt','w')
f1.write("this is 1 line\n")
f1.write("this is 2 line\n")
f1.write("this is 3 line\n")
f1.close()

f2=open('dummy.txt','a')
f2.write("\nthis is written by me")
f2.close()
