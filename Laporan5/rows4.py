n = input("Enter the number of rows: ")
m = int(n)

k = 1
for i in range(m):
    for j in range(1, i + 2):
        print(k, end=" ")
        k = k + 1
    print()