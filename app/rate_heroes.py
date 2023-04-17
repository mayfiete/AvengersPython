from flask import Flask, render_template, request

# import DbConnx from db_connx.py
from DbConnx import DbConnx

conn = DbConnx()
conn.connect()

# Construct the SQL query to insert the data into the database
query = "SELECT DISTINCT name FROM character_comic;"
# Execute the query for each row in the CSV file
conn.execute(query)

# fetch all the rows from the database
rows = conn.fetchall()

superheroes = []

# Define a list of superheroes and their ratings
# add rows to set
for row in rows:
    superheroes.append({'name': row[0], 'rating': 0})

print(superheroes)

# Define a function to calculate the average rating

app = Flask(__name__)


def get_average_rating():
    total_rating = 0
    for hero in superheroes:
        total_rating += hero['rating']
    return total_rating / len(superheroes)

# Define a route to display the list of superheroes and their ratings


@app.route('/')
def index():
    return render_template('index.html', superheroes=superheroes, average_rating=get_average_rating())

# Define a route to add a new superhero and rating


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        rating = float(request.form['rating'])
        superheroes.append({'name': name, 'rating': rating})
        return render_template('add.html', message='Superhero added successfully!')
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
