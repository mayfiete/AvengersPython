from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from DbConnx import DbConnx

app = Flask(__name__)
db_connx = DbConnx()
db_connx.connect()
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_connx.db_user}:{db_connx.db_password}@{db_connx.db_host}:{db_connx.db_port}/{db_connx.db_name}"
db = SQLAlchemy(app)


class Hero(db.Model):
    __tablename__ = 'character_comic'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = []
    for hero in heroes:
        result.append({'id': hero.id, 'name': hero.name})
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
