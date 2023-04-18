
from SuperheroClass import Superhero

# Inheritance: Villain is a subclass of Superhero
# Villain inherits all of the methods and attributes of Superhero
# Villain can override methods and attributes of Superhero
# Villain can add new methods and attributes


class Villain(Superhero):
    '''Villain class'''

    def __init__(self, name, comics=[], isVillain=True):
        super().__init__(name, comics)
        self.name = name
        self.comics = set(comics)
        self.isVillain = isVillain

    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return f'{self.name} serves evil in {len(self.comics)} comics'


# Rogue = Villain('Rogue')
# rogue_comics = Rogue.__len__()
# print(rogue_comics)


# rogue_first_comic = Rogue.__getcomics__()
# print(rogue_first_comic)
# print(Rogue.__str__())
