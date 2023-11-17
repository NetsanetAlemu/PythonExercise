from cube import Cube
from cylinder import Cylinder
from rectangular_prism import Rectangular_prism

class Solid_figures:
      
    def main(self):
        print("\nEnter 1 to calculate volume of a cube\n"
                + "Enter 2 to calculate volume of a cylinder\n"
                + "Enter 3 to calculate volume of a rectangular prism\n"
                        )
        try: 
            answer = int(input("Choose from (1, 2, or 3): "))
        except ValueError:
            print("\nEnter numbers only!\n")
        except Exception:
            print("Something went wrong!\n")
        else:

            if answer == 1:
                try:
                        
                    cu_length = float(input("\nEnter length of the cube: "))
                except ValueError:
                    print("\nEnter numbers only!\n")
                else:

                    cube = Cube(cu_length)
                    cu_area = cube.area()
                    print("\nVolume: " + str(cube.volume(cu_area, cu_length)))
            elif answer == 2:
                try:
                        
                    radius = float(input("\nEnter the radius of the cylinder: "))
                    cy_height = float(input("Enter the height of the cylinder: "))
                except ValueError:
                    print("\nEnter numbers only!\n")
                else:

                    cylinder = Cylinder(cy_height, radius)
                    cy_area = cylinder.area()
                    print("\nVolume: " + str(cylinder.volume(cy_area, cy_height)))
            elif answer == 3:
                try:
                        
                    rp_length = float(input("\nEnter length of the rectangular prism: "))
                    rp_height = float(input("Enter the height of the rectangular prism: "))
                    rp_width = float(input("Enter width of the rectangular prism: "))

                except ValueError:
                    print("\nEnter numbers only!\n")
                else:

                    rec_prism = Rectangular_prism(rp_height, rp_length, rp_width)
                    rp_area = rec_prism.area()
                    print("\nVolume: " + str(rec_prism.volume(rp_area,rp_height)))
            else:
                print("Enter your choice from (1, 2, 3) only!\n")
    def restart(self):
                  response = input("\nRestart? (yes/no): ")
                  response = response.upper()
                  if response == "YES":
                        return True
                  else:
                        return False
                        
    