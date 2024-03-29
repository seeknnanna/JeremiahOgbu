# Define a variable to store the maximum number of stars, which is 5 in this case
# Begin a for loop that iterates from 1 to the maximum number of stars, inclusive
# If the current number of stars is less than or equal to the loop index
# Print "*" multiplied by the current number of stars
# Begin a second for loop, running from the maximum number of stars minus 1 to 1, inclusive
# If the current number of stars is less than or equal to the loop index
# Print "*" multiplied by the current number of stars

# Define a variable to store the maximum number of stars
max_stars = 5

# Begin a for loop that iterates from 1 to the maximum number of stars, inclusive
for i in range(1, max_stars + 1):
    # If the current number of stars is less than or equal to the loop index
    if i <= max_stars:
        # Print "*" multiplied by the current number of stars
        print("*" * i)

# Begin a second for loop, running from the maximum number of stars minus 1 to 1, inclusive
for i in range(max_stars - 1, 0, -1):
    # If the current number of stars is less than or equal to the loop index
    if i <= max_stars:
        # Print "*" multiplied by the current number of stars
        print("*" * i)

