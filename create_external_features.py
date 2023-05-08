import csv

with open('External_Features.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['User', 'Features'])
	for i in range(500):
		writer.writerow(['user-' + str(i), 0])