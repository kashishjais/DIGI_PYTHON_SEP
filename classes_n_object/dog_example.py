class Dog:

    def __init__(self,breed,color,age,gender):
        self.breed=breed
        self.color=color
        self.age=age
        self.gender=gender
dg1=Dog('pug','off white',2,'male')
dg2=Dog('pomerian','white',5,'female')

print(dg1.breed)
print(dg2.color)
