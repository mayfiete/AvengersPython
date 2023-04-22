
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

    def __len__(self) -> int:
        return len(self.comics)

    # generator function
    def __str__(self) -> str:
        return f'{self.name} serves evil in {len(self.comics)} comics'


Juggernaut = Villain('Juggernaut')
juggernaut_comics = Juggernaut.__str__()
print(Juggernaut.__len__())
print(juggernaut_comics)
