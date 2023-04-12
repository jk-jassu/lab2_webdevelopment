# Define the height of the pattern
height = 7

# Outer loop to iterate through each row
for row in range(height):
    # Print the "#" symbol for the first column
    print("#", end="")
    
    # Inner loop to print the spaces and "#" symbols
    for col in range(row):
        # If the current row and column are equal, print "#" symbol
        if row == col:
            print("#", end="")
        # Otherwise, print a space
        else:
            print(" ", end="")
    
    # Print "#" symbol for the last column
    print("#")
