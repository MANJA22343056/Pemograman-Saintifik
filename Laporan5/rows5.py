n = input("Enter the number of rows: ")
m = int(n)

for i in range(m):
    for j in range(0, (m-i-1)):
        print(' ', end="")
    for k in range (0, 2*i+1):
        print('*', end="")
    print()