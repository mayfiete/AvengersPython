
from DbConnx import DbConnx


# import superhero data from database and then create a class for each superhero
# create a set for all of the comics that each superhero is in
# later we will use set operations to determine overlap between superheroes

class Superhero():
    '''Superhero class'''

    def __init__(self, name, comics=[]):  # comics=[] is a default argument
        self.name = name
        self.comics = set(comics)

        conn = DbConnx()

        conn.connect()

        query = "SELECT name, comic FROM character_comic WHERE name = %s;"
        conn.execute(query, (self.name,))
        rows = conn.fetchall()
        # add rows to set
        for row in rows:
            self.comics.add(row[1])

        # close the connection
        conn.close()

    def __len__(self):
        return len(self.comics)

    def __getcomics__(self):  # get a list of all of a characters comics
        return self.comics

    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return f'{self.name} is in {len(self.comics)} comics'

    # add a decorator to make this a property
    # decorators convert a method into a property
    # use only when you are calculating a value
    @property
    def count_of_comics(self):
        return len(self.comics)

    # generator function
    def __iter__(self):
        for comic in self.comics:
            yield comic


# Example usage
# Rogue = Superhero('Rogue')
# print(Rogue.name)  # Output: Spider-Man
# print(Rogue.comics)

# x = Rogue.__iter__()
# print(next(x))
# print(next(x))

# rogue_comics = Rogue.count_of_comics
# print(rogue_comics)

# Rogue = Superhero('Rogue')
# rogue_comics = Rogue.__len__()
# print(rogue_comics)


# rogue_first_comic = Rogue.__getcomics__()
# print(rogue_first_comic)
# print(Rogue.__str__())

# find comics from 2012
nci = Superhero(name="Wolverine").comics
# print(nci)
for comic in nci:
    # print(comic)
    # find comics from 2017
    if "2012" in comic:
        print(comic)
    else:
        pass

wolverine_upper_case = Superhero(name="Wolverine").comics
for comic in wolverine_upper_case:
    if "Wolverine" in comic:
        print(comic.upper())
    else:
        pass
