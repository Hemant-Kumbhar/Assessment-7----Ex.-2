import re

def is_valid_number_plate(number_plate):
    # Define the regex pattern for the number plate
    pattern = r"^[A-Z]{2} \d{2} [A-Z]{2} \d{4}$"
    
    # Check if the number plate matches the pattern
    if re.match(pattern, number_plate):
        return True
    else:
        return False

number_plate = input("Enter the vehicle number plate: ")
if is_valid_number_plate(number_plate):
    print(f"The number plate '{number_plate}' is valid.")
else:
    print(f"The number plate '{number_plate}' is invalid.")
