class Movie:
    def __init__(self,name,genre,year):
        self.name=name
        self.genre=genre
        self.year=year

    def show(self):
        print('details',self.name,self.genre,self.year)


m=Movie('free guy',['comedy','action'],2021)  
m2=Movie('done','drama',2022) 
m.show()
m2.show()     


