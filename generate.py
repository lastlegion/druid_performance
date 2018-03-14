from faker import Faker
import random
import csv
fake = Faker()


n_records = 100
data = []
r = ["Name", "Time", "Age", "Height", "Gender", "Race", "Favorite_Color", "Job", "Country", "U", "V", "W","X","Y","Z"]
for i in range(0,n_records):
	row = []
	row.append(fake.name())
	row.append(fake.date_time_between(start_date="-10d", end_date="now").isoformat())
	row.append(random.choice([10,20,30,40,50,60,70,80])) #age
	row.append(random.randint(100,200))
	row.append(random.choice(["Male", "Female"]))
	row.append(random.choice(["Asian", "African-American", "White", "Native-American"]))
	row.append(random.choice(['Red', 'Yellow', 'Green', 'Blue', 'White', 'Black']))
	row.append(random.choice(['Doctor', 'Engineer']))
	row.append(random.choice(['India', 'USA', 'England', 'Australia', 'India', 'China', 'China']))
	row.append(random.choice(['True', 'False']))
	row.append(random.choice(['Yes', 'No']))
	row.append(random.choice(['Yes','Yes','Yes', 'No']))
	row.append(random.choice([1,2,3,4,5,6]))
	row.append(random.choice([1,3,4,3,4,3]))
	row.append(random.choice([100,200,200,300]))
	data.append(row)
print(data)

with open('file.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerows(data)
