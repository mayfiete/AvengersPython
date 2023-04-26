from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from DbConnx import DbConnx
from flask_restful import Resource, Api
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)
db_connx = DbConnx()
db_connx.connect()
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_connx.db_user}:{db_connx.db_password}@{db_connx.db_host}:{db_connx.db_port}/{db_connx.db_name}"
db = SQLAlchemy(app)


class Hero(db.Model):
    __tablename__ = 'character_comic'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)


class HeroesResource(Resource):
    def get(self):
        """
        Get all heroes
        ---
        responses:
          200:
            description: A list of heroes
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
        """
        heroes = Hero.query.all()
        result = []
        for hero in heroes:
            result.append({'id': hero.id, 'name': hero.name})
        return result


api.add_resource(HeroesResource, '/heroes')

SWAGGER_URL = '/api/docs'
API_URL = '/swagger'


@app.route('/swagger')
def swagger_api():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)


# Add Swagger UI
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
