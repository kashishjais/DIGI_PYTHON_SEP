x=[90,87,65,76,23,45]
words="Python is best language to code".split()

x2=list(map(lambda i:i**2,x))

y=[4,7,5,7,9,10]
xy=list(map(lambda i,j:i+j,x,y))
print(xy)
 
 ##or
f=lambda i,j:i+j
xy=list(map(f,x,y))
print(xy)

 #filter
words_with_a=list(filter(lambda i:'a' in i,words))
print(words_with_a)


