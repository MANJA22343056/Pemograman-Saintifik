n = input("Enter the number of rows: ")
m = int(n)

k = 1
for i in range(m):
    for j in range(1, i+2):
        print(i+1, end=" ")
    print()