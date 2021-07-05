import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["Sleep in hours"]))

    return {"x" : coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml and sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Coffee.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
setup()

def getDataSource(data_path):
    marks = []
    attendance = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"]))

    return {"x" : marks, "y": attendance}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks and Attendance :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Marks.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
setup()