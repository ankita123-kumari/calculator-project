# unit=(95*71)+(30*80)+(141*78)+(122*88)+(267*126)+(150*171)
# print(f"solve this equation:{unit}")

# Simple Unit Converter

def convert_units(value, conversion_factor):
    return value * conversion_factor

# Conversion factors
conversion_table = {
    "m to cm": 100, "cm to m": 0.01,
    "kg to g": 1000, "g to kg": 0.001,
    "l to ml": 1000, "ml to l": 0.001
}

# Display available conversions
print("\nAvailable conversions:")
for conversion in conversion_table.keys():
    print(f"- {conversion}")

# Get user input
conversion_type = input("\nEnter conversion type (e.g., 'm to cm'): ").strip().lower()
value = float(input("Enter value to convert: "))

# Perform conversion
if conversion_type in conversion_table:
    result = convert_units(value, conversion_table[conversion_type])
    print(f"\nConverted Value: {value} {conversion_type.split()[0]} = {result:.2f} {conversion_type.split()[2]}")
else:
    print("\nInvalid conversion type. Please choose from the list.")