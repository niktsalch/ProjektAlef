import database
import pandas as pd #Datenverarbeitung und -analyse
import glob #zum Suchen von Dateien

database.db_obj.execute("DROP TABLE IF EXISTS sensor")
#Tabelle wird gelöscht
database.db_obj.execute("""
    CREATE TABLE IF NOT EXISTS sensor (
        sensor_id       INTEGER,
        sensor_type     TEXT,
        location        INTEGER,
        lat             REAL,
        lon             REAL,
        timestamp       TEXT,
        P1              REAL,
        durP1           INTEGER,
        ratioP1         REAL,
        P2              REAL,
        durP2           INTEGER,
        ratioP2         REAL
    )
""")
#Tabelle wird erstellt
for csv_file in glob.glob("*.csv"):
    df = pd.read_csv(csv_file, header = 1, delimiter = ";")
    #Daten werden gelesen
    df.columns = ["sensor_id", "sensor_type", "location", "lat", "lon", "timestamp", "P1", "durP1", "ratioP1", "P2", "durP2", "ratioP2"]
    #Werte werden gesetzt
    df.to_sql("sensor", database.db_obj.connection, if_exists = "append", index = False)
    #Daten umwandeln in SQL. Daten werden in Tabelle eingetragen


database.db_obj.connection.commit()
database.db_obj.connection.close()