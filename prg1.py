"""
Write a function that takes the lengths of three sides: side1, side2 and side3 of the
triangle as the input from the user using input function and return the area of the
triangle as the output. Also, assert that sum of the length of any two sides is greater
than the third side.
"""

side1 = int (input("Enter the first side of the triangle: "))
side2 = int (input("Enter the second side of the triangle: "))
side3 = int (input("Enter the third side of the triangle: "))

def tri (sd1, sd2, sd3):
    s = (sd1 + sd2 + sd3)/2
    ar = ((s*(s - sd1)*(s -sd2)*(s -sd3))**0.5)
    pr = s*2
    return ar , pr

area, perimeter = tri(side1, side2, side3)
print("Area of the triangle:", area,"\nPerimeter of the triangle: " ,perimeter)
