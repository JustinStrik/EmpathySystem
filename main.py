import csv
import decimal
import locale

# Open the input CSV file
with open('physconst.csv', 'r') as input_file:
  # Create a reader object to parse the file
  reader = csv.reader(input_file)

  # Open the output CSV file
  with open('output.csv', 'w') as output_file:
    # Create a writer object to write to the file
    writer = csv.writer(output_file)

    # Loop through each row in the input file
    for row in reader:
      # Get the first value in the row (the number in scientific notation)
      value = row[0]

      # Remove any spaces in the value
      value = value.replace(" ", "")

      # Try to split the value into two parts: the number and the exponent
      try:
        number, exponent = value.rsplit("e", 1)
      except ValueError:
        # If the value does not contain the character 'e', use the whole value as the number
        number = value
        exponent = 0

      # If the exponent is present, convert it to a decimal
      if exponent:
        exponent = decimal.Decimal(exponent)
      else:
        # If the exponent is not present, set it to 0
        exponent = 0

      # Convert the number to a floating point value
      float_value = locale.atof(number)

      # Convert the float value to a decimal and adjust it by the exponent
      decimal_value = decimal.Decimal(float_value) * (10 ** exponent)

      # Write the decimal value to the output file
      writer.writerow([decimal_value])
