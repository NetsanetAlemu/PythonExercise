# challenge 1
# print 
# 1
# 22
# 333
# 4444
# 55555
rows = int(input("Enter rows: "))

for i in range(1,rows + 1):
    for j in range(i):
        print(i, end = " ")
    print()

#challenge 2: print
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

#challenge 3: print 
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

rows = int(input("Enter rows: "))
for i in range(1, rows + 1):
    for j in range(rows , i - 1, -1):
        print(i, end = " ")
    print()

#challenge 4: print 
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
rows = int(input("Enter rows: "))
symbol = input("Enter symbol: ")
for i in range(1, rows + 1):
    for j in range(rows , i - 1, -1):
        print(symbol, end = " ")
    print()





    

