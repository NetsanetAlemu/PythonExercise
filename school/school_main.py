from school import School

school_1 = School("ADM school", 1993, "Private")
school_2 = School("STEM center", 2004, "Public")

titles = ("Name", "Year", "Type", "City")

schol_1 = (school_1.name, school_1.year, school_1.type, school_1.city)

schol_2 = (school_2.name, school_2.year, school_2.type, school_2.city)

print()
for i in titles:
    print("{:<20}".format(i), end = "")
print()
for i in schol_1:
    print("{:<20}".format(i), end = "")
print()
for i in schol_2:
    print("{:<20}".format(i), end = "")
















