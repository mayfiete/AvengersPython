
from SuperheroClass import Superhero

# class generator


class NextComicToRead(Superhero):
    '''NextComicToRead class'''

    def __init__(self, name, comics=[]):
        self.name = name
        self.comics = set(comics)
        self.next_comic = None

    def __repr__(self) -> str:
        return f'{self.name}'

    def add_comic(self, comic):
        self.comics.add(comic)

    def __str__(self) -> str:
        return f'{self.name} has {len(self.comics)} comics'

    def __len__(self) -> int:
        return len(self.comics)

    def __iter__(self):
        for comic in self.comics:
            yield comic

    # new for Python 3
    def __next__(self):
        return self.next_comic


# Example usage
Rogue = NextComicToRead('Rogue')
Rogue.add_comic('X-Men #1')
Rogue.add_comic('Avengers #100')
print(Rogue)
print(list(Rogue))  # ['X-Men #1', 'Avengers #100']
x = Rogue.__iter__()
print(next(x))
print(next(x))
