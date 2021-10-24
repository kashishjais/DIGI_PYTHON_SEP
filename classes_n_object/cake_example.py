class cake:
    brand ="JJ bakery"
    flavour="chocolate"
    weight=1
    is_eggless=False
    color='brown'

cake1=cake() #object 1
cake2=cake() #object 2
print(cake1) #will print reference of objects
print(cake2)

print(cake1.flavour)
cake2.flavour="strawberry"
print(cake2.flavour)
