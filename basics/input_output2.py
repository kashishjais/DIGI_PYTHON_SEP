a=10
b="balls"
c=100
d="rupees"
#printing with comma separation
print("raju purchased",a,b,"for",c,d)
#concatination
print("raju purchased "+ str(a)+ ' '+ b + " for " + str(c) + ' '+d)
#format specifier
print("raju purchased %d %s for  %d %s"%(a,b,c,d))
#format func()
print("raju purchased {} {} for {} {}".format(a,b,c,d))
#f string
print(f'raju purchased {a} {b} for {c} {d}')
# use of end and sep
print("hiii",end=' ')
print("there")
print(a,b,c,d,sep="🤷‍♂️")