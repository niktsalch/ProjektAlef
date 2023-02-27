import sqlite3

class Database():
    def __init__(self, db):
        self.db = db
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()  

    def fetch(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

db_obj = Database("C:\sqlite\sensor.db")
