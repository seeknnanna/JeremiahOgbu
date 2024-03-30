# Ask user for the number of rows for the pattern and convert it to an integer.
max_stars = int(input("Enter the number of rows for the pattern: "))
# Function to print pattern and save to a file.
def print_and_save_pattern(rows):
    pattern_output = ''
    for i in range(1, rows + 1):
        pattern_output += '*' * i + '\n'
    for i in range(rows - 1, 0, -1):
        pattern_output += '*' * i + '\n'
    
    print(pattern_output)
    
    # Save the pattern to a text file
    with open('pattern_output.txt', 'w') as file:
        file.write(pattern_output)

# Use the function
print_and_save_pattern(max_stars)
# Validate that the user input is a positive integer.
try:
    max_stars = int(input("Enter the number of rows for the pattern: "))
    if max_stars <= 0:
        raise ValueError
except ValueError:
    print("Please enter a positive integer.")
    exit()
