import csv

with open ('C:\Users\HP\Desktop\python\biblewords.csv','r',encoding="utf-8") as csv_file:
    reader =csv.reader(csv_file)
    #next(reader) # skip first row
    for row in reader:
        print(row)
