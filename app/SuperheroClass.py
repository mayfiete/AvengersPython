
from DbConnx import DbConnx


# import superhero data from database and then create a class for each superhero
# create a set for all of the comics that each superhero is in
# later we will use set operations to determine overlap between superheroes

class Superhero():
    '''Superhero class'''

    def __init__(self, name, comics=[]):
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

    # def count_of_comics(self):
    #     return len(self.comics)


# Example usage
# Rogue = Superhero('Rogue')
# print(Rogue.name)  # Output: Spider-Man
# print(Rogue.comics)

# rogue_comics = Rogue.count_of_comics()
# print(rogue_comics)
