from flask_restful import Resource, reqparse
import sqlite3
import os

class NewHighscore(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nickname', type=str, required=True)
        parser.add_argument('score', type=int, required=True)
        args = parser.parse_args()

        # Query db
        conn = sqlite3.connect(os.getenv('DB_PATH', './../highscores.db'))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM highscores")
        current_highscores = [{"nickname": x[0], "score": x[1]} for x in cursor.fetchall()]
        should_add = True
        for i in range(len(current_highscores)):
            score = current_highscores[i]

                if score["nickname"] == args["nickname"]:
                    should_add = False
                        if score["score"] <= args["score"]:
                            current_highscores.pop(i)
                                current_highscores.append(args)

        if should_add:
            current_highscores.append(args)

        # Sorts highscores and trims list to length 10
        sorted_list = sorted(current_highscores, key=lambda k: k['score'], reverse=True)
        sorted_list = sorted_list[:10]

        cursor.execute("DELETE FROM highscores")
        for score in sorted_list:
            query = "INSERT INTO highscores VALUES ('{}', {})".format(score["nickname"], score["score"])
                cursor.execute(query)

        conn.commit()
        conn.close()

        return args
