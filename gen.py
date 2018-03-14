import csv
import datetime
import random
Data = []
with open('trial.csv') as f:
	fr = csv.reader(f)
	for row in fr:
		startDate = datetime.datetime(2018, 1, 1)+ datetime.timedelta(days=random.randint(0,100))+ datetime.timedelta(minutes=random.randint(0,55))+datetime.timedelta(hours=random.randint(0,22)) + datetime.timedelta(seconds=random.randint(0,55))
		row[-6] = startDate.isoformat()
		Data.append(row)

with open('trial5.csv', 'w') as f:
	fw = csv.writer(f)
	fw.writerows(Data)
