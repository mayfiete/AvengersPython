
import subprocess
from archive_hero_names import ArchiveHeroNames

scripts_to_execute = [
    'app/fetch_heroes.py',
    'app/format_json.py',
    'app/persist.py',
    'app/write_to_mongodb.py',
    'app/pivot_db_data.py'
]

for script in scripts_to_execute:
    subprocess.call(['python', script])

ArchiveHeroNames('C:\\AvengersPython\\app\\hero_names.txt', 'C:\\AvengersPython\\archive_hero_names.txt').archive_hero_names() 

# Path: app\fetch_heroes.py
