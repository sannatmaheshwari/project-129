import csv
dataset1 = []
dataset2 = []
with open("final.csv","r") as f:
    reader = csv.reader(f)
    for x in reader:
        dataset1.append(x)
with open("archivefinal.csv","r") as af:
    final = csv.reader(af)
    for i in final:
        dataset2.append(i)
headers1 = dataset1[0]
planetdata1 = dataset1[1:]
headers2 = dataset2[0]
planetsdata2 = dataset2[1:]
headers = headers1+headers2
planetsdata = []
for index,row in enumerate(planetdata1):
    planetsdata.append(planetdata1[index]+planetsdata2[index])
with open("merged.csv","a+") as m:
    writer = csv.writer(m)
    writer.writerow(headers)
    writer.writerows(planetsdata)