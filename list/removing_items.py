#REMOVING
# serching value-- use with if condition
colors=['red','blue','yellow','green','pink','black','pink']
colors.remove("yellow")
print(colors)
if 'pink' in colors:
    colors.remove('pink') #will remove only first occurrence of pink
print(colors)

#POP
# remove value by index
# poped value can be stored in any variable unlike remove
colors.pop(1)
print(colors)
poped_val=colors.pop(3)
print(colors)
print(poped_val)
# clear
colors.clear()
print(colors)


