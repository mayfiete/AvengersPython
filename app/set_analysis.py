# C:\AvengersPython\app\SuperheroClass.py
from SuperheroClass import Superhero as sh

hero1 = sh('Rogue')
hero2 = sh('Wolverine')

shared_comics = hero1.comics.intersection(hero2.comics)

print(shared_comics)
