
# importing the csv module
import csv


with open('input.csv', 'r', encoding='utf-8-sig') as read_obj: 

	# Return a reader object which will 
	# iterate over lines in the given csvfile 
	csv_reader = csv.reader(read_obj) 

	# convert string to list 
	list_of_csv = list(csv_reader) 
	integers = list_of_csv[0]
	equations = list_of_csv[1:]

	# print(integers) 
	# print(equations)


dictionary = {}
i = 0
while i < len(characters):
	dictionary.update({characters[i]: int(integers[i])})
	i+=1

values = []
rows = [integers]
for row in equations:
	values = []
	for eqn in row:
		value = eval(eqn, dictionary)
		values.append(value)
		# print(value)
	rows.append(values)

print(rows)

filename = "records.csv"


# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv writer object
	csvwriter = csv.writer(csvfile)

	# writing the data rows
	csvwriter.writerows(rows)

