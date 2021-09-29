name="vijay deenanath chauhan"
print(len(name))
print(name[2:5])
print(name[6:15])
print(name[6:-8])
#we can skip value before colon if we want to print from beginning
#we can skip value after colon if we want to print till end
print(name[:5])
print(name[-7:])
# syntax for slicing
# var[startidx:endidx:gap]
print(name[::2])#start to end with gap 2

##reverse string
print(name[::-1])
print(name[:])
print(name[:][::-1][:5])
