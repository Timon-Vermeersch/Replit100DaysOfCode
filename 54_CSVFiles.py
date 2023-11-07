import csv

fileName = "annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv"
total = 0.0

with open(fileName,newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["year"])