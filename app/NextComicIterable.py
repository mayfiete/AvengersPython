
from SuperheroClass import Superhero
from NextComicToRead import NextComicToRead

# Simply put, an iterator is an object that implements the iterator protocol,
# similar to how a sequence implements the sequence protocol.


class NextComicIterable(Superhero):
    def __init__(self, name, comics=[]):
        self.name = name
        self.comics = set(comics)
        self.next_comic = None

    def __len__(self):
        return len(self.comics)

    def __getitem__(self, index):
        return self.comics[index]


nci = NextComicIterable(name="Wolverine")

# iterate over the comics in the NextComicIterable object
for comic in nci:
    print(comic)

# find comics from 2017
for comic in nci:
    filtered_strings = list(filter(lambda x: '2017' in x, comic))
    print(filtered_strings)
