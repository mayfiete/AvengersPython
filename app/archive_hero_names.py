import pandas as pd


class ArchiveHeroNames():
    '''This class is used to archive the hero names'''

    def __init__(self, hero_names_file, archive_hero_names_file):
        self.hero_names_file = hero_names_file
        self.archive_hero_names_file = archive_hero_names_file

    def archive_hero_names(self):
        with open(self.hero_names_file, 'r') as f:
            contents = f.read()

        with open(self.archive_hero_names_file, 'a') as f:
            f.write(contents)

# ArchiveHeroNames('C:\\AvengersPython\\app\\hero_names.txt', 'C:\\AvengersPython\\archive_hero_names.txt').archive_hero_names()

# # open the hero.txt file and copy the contents to another text file
# with open('C:\\AvengersPython\\app\\hero_names.txt', 'r') as f:
#     contents = f.read()

# # copy to another text file
# with open('C:\\AvengersPython\\archive_hero_names.txt', 'a') as f:
#     f.write(contents)
