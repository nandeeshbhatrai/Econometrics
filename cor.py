import csv

x = {1:31,   2:28, 3:31,    4:30,   5:31,  6:30, 7:31,    8:31,   9:30,  10:31,    11:30,  12:31}

def leap(year: int) -> bool:
	return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

input_file = 'economictimes2.csv'

# Read the data from the input CSV file
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Process the data
for row in data:
    # Decrease the value of the 3rd field (day) by 1
    row[2] = str(int(row[2]) - 1)
    if row[2] == '0':
        row[1] = str(int(row[1]) - 1)
        if row[1] == '0':
            row[1] = '12'
            row[0] = str(int(row[0]) - 1)
        if(leap(int(row[0])) and row[1] == '2'):
            row[2] = '29'
        else:
            row[2] = str(x[int(row[1])])
             


# Write the updated data back to the same CSV file
with open(input_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("The day field has been decremented by 1 for all rows.")
