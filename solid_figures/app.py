from solid_figures import Solid_figures

solid_figures = Solid_figures()

solid_figures.main()

while solid_figures.restart():
    solid_figures.main()

print("\nBye!\n")