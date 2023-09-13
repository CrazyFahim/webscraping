# crteate a csv file to store the data

import csv

with open('data.csv', 'w', newline='') as file:
    wrt = csv.writer(file)
    wrt.writerow(
        ["Date", "Time", "Temperatire", "Dew Point", "Humidity", "Wind", "Wind Speed", "Wind Gust", "Pressure", "Precip", "Condition"]
    )
