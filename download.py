import datetime
import requests

year = 2022

for day in range(1, 366):
    date = datetime.date(year, 1, 1) + datetime.timedelta(day - 1)  #Berechne das Datum für den aktuellen Tag im Schleifenlauf
    month = date.month  #Hole den Monat aus dem Datum
    day = date.day  #Hole den Tag aus dem Datum
    
    if month < 10:
        month = "0" + str(month)  #Füge eine führende Null hinzu, wenn der Monat einstellig ist
    
    if day < 10:
        day = "0" + str(day)  #Füge eine führende Null hinzu, wenn der Tag einstellig ist
    
    url = f"https://archive.sensor.community/{year}/{year}-{month}-{day}/{year}-{month}-{day}_yearsds011_sensor_92.csv"  #Baue die URL für den Download zusammen
    
    response = requests.get(url)  #Sende eine GET-Anfrage an die URL, um die Datei herunterzuladen
    
    if response.status_code == 200:  #Überprüfe, ob die Anfrage erfolgreich war (Statuscode 200)
        with open(f"{year}-{month}-{day}_sds011_sensor_141.csv", "wb") as f:  #Öffne eine Datei im Binärmodus zum Schreiben
            f.write(response.content)  #Schreibe den Inhalt der heruntergeladenen Datei in die lokale Datei
        print(f"Heruntergeladen {year}-{month}-{day}_sds011_sensor_141.csv")
    else:
        print(f"Fehler beim Herunterladen von {year}-{month}-{day}_sds011_sensor_141.csv")