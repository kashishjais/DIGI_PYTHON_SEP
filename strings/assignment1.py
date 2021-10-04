name="Kashish Jaiswal" #solution 1
print(name)

string=input("enter a string to find its length: ")  #solution 2
print(len(string))

line="Python is great" #solution 3
line[10:]

line2="Python is everywhere" #solution 4
print(line2.replace(' ','\n'))

a="Hello World!" #solution 5
a[::-1]

print("How are you?".upper()) #solution 6

print("How Is It Going?".lower()) #solution 7

words=['Python','is','easy','to','learn'] #solution 8
' '.join(words)

print('''this is to show....... 
a multi line string .....
using a single print .....''') #solution 9

print("to move to newline "+'\n'+ 'is used') #solution 10

variable=23 #solution 11
print(f'the variable is {variable}')

s1='python'  #solution 12
s2='is'
s3='great'
print(s1+s2+s3)

print('#'*20) #solution 13

for i in range(1,10):    #solution 14
  print(i,end='.\n')

s=input("enter a sentence") #solution 15
print(s.replace(' ','\n'))

string2=input("enter your string to check")  #solution 16
if string2[-1]=='?':
  print("yes")

s3=input('enter your string to count e: ')  #solution 17
c=0
for i in s3:
  if i=='e':
    c+=1 
print(f'e is present {c} times')    

n=input("enter your data: ")  #solution 18
if n.isnumeric():
  print("yes it is a number")
else:
  print("not a number")  

text='    this is not a good string         ' #solution 19
text.strip("    ")

new=input("enter your string: ") #solution 20
for i in new:
  if i.isupper():
    print("found")

names='Joe,David,Mark,Tom,Chris,Robert' #solution 21
list=names.split(',')
print(list)

text2='this is some text' #solution 22
updated_text=text2.replace(' ','aye ')
print(updated_text)


user_s=input("enter your string: ") #solution 23
if user_s.find('fyi')!=-1:
  print("yes")
else:
  print("no")  


text3='%p34@y!*-*!t68h#&on404' #solution 24
punc='!@#$%^&*()_-1234567890'
for i in text3:
  if i not in punc:
    print(i,end='')


#solution 25
para2='this is a paragraph which is written just for the purpose of providing context to let the average word lenghth be calculated'
words=para2.split(' ')
t=len(words)
s=0
for i in words:
  l=len(i)
  s+=l  
avg=s//t
print(f'average word length is {avg} ') 

