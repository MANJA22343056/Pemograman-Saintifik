n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

for i in range(n):
    for j in range(m):
        element = 5*(i+j)*(i+j)
        print(element, sep =' ', end=' ')
    print()