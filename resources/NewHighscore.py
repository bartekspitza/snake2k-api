from flask_restful import Resource
import sqlite3

class NewHighscore(Resource):
	def post(self):
		return {"nickname": "bartek", "score": "2200"}
