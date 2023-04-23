import database
import datetime
import matplotlib.pyplot as plt
import numpy

#Definiere eine Klasse zur Visualisierung von Sensordaten
class Visiualizer:
    def __init__(self): #Initialisiere Start- und Enddatum-Attribute mit None
        self.start_date = None
        self.end_date = None
    
    def fetch_sensordata(self):  #Definiere eine Methode zum Abrufen von Sensordaten aus der Datenbank
        #Rufe Daten aus der Datenbank unter Verwendung der Start- und Enddaten ab
        self.data = database.db_obj.fetch_pvalues_by_month(self.start_date, self.end_date)
        #Extrahiere Monat, P1- und P2-Werte aus den abgerufenen Daten und speichere sie als Klassenattribute
        self.months = [x[0] for x in self.data]
        self.avg_p1 = [x[1] for x in self.data]
        self.avg_p2 = [x[2] for x in self.data]
    
    #Definiere eine Methode zur Darstellung der Sensordaten
    def data_plot(self):
        #Setze Start- und Enddatum für die abzurufenden und darzustellenden Daten
        self.start_date = datetime.datetime(2022, 1, 1)
        self.end_date = datetime.datetime(2022, 12, 31)
        #Rufe mit der fetch_sensordata-Methode die Daten für die angegebenen Daten ab
        self.fetch_sensordata()
        #Setze die Breite jeder Säule im Diagramm
        bar_width = 0.35
        #Setze die Positionen der Säulen für jeden Monat
        r1 = numpy.arange(len(self.months))
        r2 = [x + bar_width for x in r1]
        #Erstelle ein Balkendiagramm mit zwei Säulen pro Monat, eine für P1 und eine für P2
        plt.bar(r1, self.avg_p1, color='#7f6d5f', width=bar_width, edgecolor='white', label='P1')
        plt.bar(r2, self.avg_p2, color='#557f2d', width=bar_width, edgecolor='white', label='P2')
        #Setze die Beschriftungen für die x- und y-Achse sowie den Diagrammtitel
        plt.xlabel('Month')
        plt.ylabel('Average PM Values')
        plt.title('Average PM Values by Month')
        #Setze die Tick-Beschriftungen auf die Monatsnamen und zeige die Legende an
        plt.xticks([r + bar_width for r in range(len(self.months))], self.months)
        plt.legend()
        #Zeige das Diagramm an
        plt.show()

#Erstelle eine Instanz der Visualizer-Klasse und rufe ihre data_plot-Methode auf
obj = Visiualizer()
obj.data_plot()