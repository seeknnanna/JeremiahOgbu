# Define a variable to store the maximum number of layers in the pattern, which is 5 in this case
peak_star_count = 5

# Generate a star pattern that increases to the peak and decreases
# Each line prints a number of stars (*) that corresponds to the line number
# until the peak is reached and then reduces in the same pattern
for i in range(1, peak_star_count * 2):
    # Calculate the number of stars for the current line
    # The pattern first scales up to the peak_star_count and then scales down
    star_count = peak_star_count - abs(peak_star_count - i)
    print("*" * star_count)
