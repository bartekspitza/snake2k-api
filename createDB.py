import sqlite3

conn = sqlite3.connect('highscores.db')
c = conn.cursor()

create_table_query = "CREATE TABLE highscores (name TEXT, score INTEGER)"
c.execute(create_table_query)
