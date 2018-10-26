from flask_restful import Resource

class NewHighscore(Resource):
	def post(self):
		
		return {"nickname": "bartek", "score": "2200"}
