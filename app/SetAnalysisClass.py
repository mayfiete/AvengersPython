# if you like a hero, find the other heroes that share the same comic books
from SuperheroClass import Superhero as sh


# create a class to look at the intersection of two sets
class SetAnalysis:
    def __init__(self, hero1=None, hero2=None):
        self.hero1 = hero1 or sh('Rogue', ['X-Men', 'Avengers'])
        self.hero2 = hero2 or sh('Wolverine', ['X-Men', 'X-Force'])

    def intersection(self):
        return self.hero1.comics.intersection(self.hero2.comics) 
    
    def union(self):
        return self.hero1.comics.union(self.hero2.comics)
    


# x = SetAnalysis().intersection()
# print(x)

# y = SetAnalysis(sh('Rogue'), sh('Wolverine')).intersection()
# print(y)
