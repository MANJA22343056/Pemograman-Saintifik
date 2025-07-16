a = int(input("Enter the first term of the Geometric Progression\t: "))
r = int(input("Enter the common ratio\t: "))
n = int(input("Enter the number of terms\t: "))

i = 1
sum = 0  # initialize
while i <= n:
    term = a * (r** (i-1))
    print("The " + str(i) + "the term is " + str(term))
    sum = sum + term
    i = i + 1
else:
    print("The sum of " + str(n) + " term is\t: " + str(sum))