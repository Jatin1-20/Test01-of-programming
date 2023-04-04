# Define global variables for primary colors
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

# Get user inputs for color1 and color2
color1 = input("Enter the first primary color in lower case: ")
color2 = input("Enter the second primary color in lower case: ")

# Validate user inputs
if color1 not in [RED, BLUE, YELLOW]:
    print("Error: The first color you entered is invalid.")
elif color2 not in [RED, BLUE, YELLOW]:
    print("Error: The second color you entered is invalid.")
elif color1 == color2:
    print("Error: The two colors you entered are same")
else:
    # Mix the primary colors
    if color1 == RED and color2 == BLUE or color1 == BLUE and color2 == RED:
        print("PURPLE")
    elif color1 == RED and color2 == YELLOW or color1 == YELLOW and color2 == RED:
        print("ORANGE")
    elif color1 == BLUE and color2 == YELLOW or color1 == YELLOW and color2 == BLUE:
        print("GREEN")
    else:
        print("Error: Invalid combination of colors")
