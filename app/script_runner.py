
import subprocess

scripts_to_execute = [
    'app/fetch_heroes.py',
    'app/format_json.py',
    'app/persist.py',
    'app/pivot_db_data.py'
]

for script in scripts_to_execute:
    subprocess.call(['python', script])

# Path: app\fetch_heroes.py
