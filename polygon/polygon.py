from triangle_area import Traingle_area
from triangle_perimeter import Triangle_perimeter
from rectangle import Rectangle
from square import Square
from circle import Circle
from interior_angle import Interior_angle


class Polygon:
      def main(self):
            print("\nEnter 1 to calculate area of right angle triangle\n"
                  + "Enter 2 to calculate perimeter of a triangle\n"
                  + "Enter 3 to calculate area and perimeter of rectangle\n"
                  + "Enter 4 to calculate area and perimeter of a square\n"
                  + "Enter 5 to calculate area and circumfrence of a circle\n"
                  + "Enter 6 to calculate sum of interior angles\n"
            )
            try: 
                  answer = int(input("Choose from (1, 2, 3, 4, 5, or 6): "))
            except ValueError:
                  print("Enter numbers only!")
            except Exception:
                  print("Something went wrong!")
            else:

                  if answer == 1:
                        try:
                        
                              base = int(input("\nEnter length of the base: "))
                              height = int(input("Enter length of the height: "))
                        except ValueError:
                              print("Enter numbers only!")
                        else:

                              triangle = Traingle_area(base, height)

                              print(
                              "\nArea of a traingle with side lengths "
                              + str(base)
                              + ", and "
                              + str(height)
                              + " is "
                              + str(triangle.triaangle_area())
                              + "\n"
                              )

                  elif answer == 2:
                        try:
                              side1 = float(input("\nEnter length of side 1: "))
                              side2 = float(input("Enter length of side 2: "))
                              side3 = float(input("Enter length of side 3: "))

                        except ValueError:
                              print("Enter numbers only!")
                        else: 
                              triangle = Triangle_perimeter(side1, side2, side3)

                              print(
                              "\nPerimeter of a traingle with side lengths "
                              + str(side1)
                              + ", "
                              + str(side2)
                              + ", and "
                              + str(side3)
                              + " is "
                              + str(triangle.triangle_perimeter())
                              + "\n"
                              )
                  elif answer == 3:
                        try:
                              length = float(input("\nEnter length: "))
                              width = float(input("Enter width: "))
                        except ValueError:
                              print("Enter numbers only!")
                        else:
                              rectangle = Rectangle(length, width)

                              print("\nArea: " + str(rectangle.rectangle_area()))
                              print("Perimeter: " + str(rectangle.rectangle_perimeter()) + "\n")
                  elif answer == 4:
                        try:
                              length = float(input("\nEnter legth of side of the square: "))
                        except ValueError:
                              print("Enter numbers only!")
                        else:
                              square = Square(length)

                              print("\nArea: " + str(square.square_area()))
                              print("Perimeter: " + str(square.square_perimeter()) + "\n")
                  elif answer == 5:
                        try:
                              radius = float(input("\nEnter radius of the circle: "))
                        except ValueError:
                              print("Enter numbers only!")
                        else:
                              circle = Circle(radius)

                              print("\nArea: " + str(circle.area()))
                              print("Circumference: " + str(circle.perimeter()) + "\n")
                  elif answer == 6:
                        try:
                              side = int(input("\nEnter number of sides of the regular polygon: "))
                        except ValueError:
                              print("Enter numbers only!")
                        else:
                              polygon = Interior_angle(side)

                              print("Sum of interior angles: " + str(polygon.interior_angle_sum()) + "°\n")
                  else:
                        print("Enter your choice from (1, 2, 3, 4, 5, 6) only!")

      def restart(self):
                  response = input("Restart? (yes/no): ")
                  response = response.upper()
                  if response == "YES":
                        return True
                  else:
                        return False

                  