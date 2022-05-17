import csv

data = []
with open("archive_dataset.csv","r") as a:
    archive = csv.reader(a)
    for x in archive:
        data.append(x)
headers = data[0]
planetdata = data[1:]
for x in planetdata:
    x[2]=x[2].lower()
planetdata.sort(key = lambda planetdata:planetdata[2])
with open("archive.csv","a+") as y:
    archive = csv.writer(y)
    archive.writerow(headers)
    archive.writerows(planetdata)
