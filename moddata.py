import csv

# Open the input CSV file
with open('Fundamental-Physical-Constants.csv', 'r') as input_file:
  # Create a CSV reader
  reader = csv.reader(input_file)
  
  # Read the rows into a list
  rows = list(reader)

# Iterate over the rows and remove any that do not have "Constant" in the A column
rows = [row for row in rows if "Constant" in row[0]]

print("hi")

print(rows[0][0])
for row in rows:
  print(row[0])

# Open the output CSV file
with open('outputConst.csv', 'w', newline='') as output_file:
  # Create a CSV writer
  writer = csv.writer(output_file)
  
  # Write the modified rows to the output file
  writer.writerows(rows)
