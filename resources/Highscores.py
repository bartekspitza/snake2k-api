from flask_restful import Resource
import sqlite3
import os

class Highscores(Resource):
    def get(self):
        path = os.getenv('DB_PATH', './../highscores.db')
        conn = sqlite3.connect(path)
        c = conn.cursor()

        c.execute("SELECT * FROM highscores")
        highscores = [{"nickname": x[0], "score": x[1]} for x in c.fetchall()]

        return highscores
