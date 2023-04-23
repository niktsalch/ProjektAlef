import sqlite3

class Database():
    def __init__(self, db):
        self.db = db #Speichere den Dateipfad der Datenbank
        self.connection = sqlite3.connect(self.db) #Verbindung zu SQL Datenbank
        self.cursor = self.connection.cursor() #Der Cursor der Datenbank wird in einer Variable gespeichert

    def fetch(self, query):
        self.cursor.execute(query) #Führe die Abfrage aus
        return self.cursor.fetchall() #Hole alle Ergebnisse aus dem Cursor und gib sie zurück

    def execute(self, query):
        self.cursor.execute(query) #Führe die Abfrage aus
        self.connection.commit() #Übertrage die Änderungen zur Datenbank
    
    def fetch_pvalues_by_month(self, startdate, enddate):
        query = """
            SELECT
                strftime('%Y-%m', timestamp) AS month,
                AVG(P1) AS avg_p1,
                AVG(P2) AS avg_p2
            FROM
                sensor
            GROUP BY
                month
        """
        self.cursor.execute(query) #Führe die Abfrage aus
        return self.cursor.fetchall() #Hole alle Ergebnisse aus dem Cursor und gib sie zurück
        

db_obj = Database("C:\sqlite\sensor.db") #__init__ wird hier ausgeführt, um ein Objekt zu bauen