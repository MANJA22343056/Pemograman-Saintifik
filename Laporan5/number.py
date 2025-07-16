a = int(input('Enter the first number: '))
b = int(input("Enter the second number: "))
power = 1
i = 1
while i <= b:
    power = power*a
    i = i + 1
else:
    print(str(a)+' to the power of '+str(b)+' is '+ str(power))