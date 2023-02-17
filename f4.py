import csv
filename = open('departments.csv', 'r')
file = csv.DictReader(filename)
department_id = []
department_name = []
for col in file:
	department_id.append(col['department_id'])
	department_name.append(col['department_name'])
	
print('ID:', department_id)
print('Name:', department_name)

