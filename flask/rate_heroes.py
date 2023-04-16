from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of superheroes and their ratings
superheroes = [
    {'name': 'Superman', 'rating': 8.5},
    {'name': 'Spiderman', 'rating': 9.0},
    {'name': 'Batman', 'rating': 8.0},
    {'name': 'Wonder Woman', 'rating': 8.5},
]

# Define a function to calculate the average rating


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
