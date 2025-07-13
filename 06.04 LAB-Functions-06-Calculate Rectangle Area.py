# Create a function that calculates and returns the area of a rectangle by a given width and height.
# Print the result on the console.

width = int(input("Enter width: "))
height = int(input("Enter height: "))


def calculate_area(width, height):
    area = width * height
    return area


print(calculate_area(width, height))