from circle import Circle

try:
    radius = float(input("Enter radius of a circle: "))
    circle_1 = Circle(radius)
    print("Radius: " + str(radius))
    print("Perimeter: " + str(circle_1.perimeter()))
    print("Area: " + str(circle_1.area()))
except ValueError:
    print("Enter valid radius value! (\" Enter numbers only!\")")