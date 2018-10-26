from flask_restful import Resource

class Highscores(Resource):
	def get(self):
		highscore = {"nickname": "bartek", "score": "100"}


		return highscore
