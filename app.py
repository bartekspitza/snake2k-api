from flask import Flask
from flask_restful import Resource, Api
from resources.Highscores import Highscores
from resources.NewHighscore import NewHighscore

app = Flask(__name__)
api = Api(app)

api.add_resource(Highscores, '/api/')
api.add_resource(NewHighscore, '/api/newhighscore')


if __name__ == '__main__':
<<<<<<< HEAD
	app.run(debug=True)
=======
	app.run()
>>>>>>> 6bc265038490e15640bda22bf51e0e71770cdd17
