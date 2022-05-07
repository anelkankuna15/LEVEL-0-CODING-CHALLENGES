# function that takes in a number representing the temperature in Celsius and returns the temperature in Fahrenheit.
#  Write another function that does the opposite (Fahrenheit to Celsius).

temp = input("Enter  temperature to convert from Fahreit to Celcius? (e.g., 66F, 145C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
