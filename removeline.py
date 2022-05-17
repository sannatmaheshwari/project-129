import csv

with open("merged.csv") as input,open("mergedfinal.csv","w",newline="") as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)