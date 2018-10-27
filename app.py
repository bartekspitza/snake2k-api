from flask import Flask
from flask_restful import Resource, Api
from resources.Highscores import Highscores
from resources.NewHighscore import NewHighscore

app = Flask(__name__)
api = Api(app)
		
api.add_resource(Highscores, '/api/')
api.add_resource(NewHighscore, '/api/newhighscore')

if __name__ == '__main__':
	app.run(debug=True)
