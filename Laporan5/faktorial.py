n = input ('Enter number whose factorial is required: ') # task user to enter number
m = int(n) # convert the input to an integer
factorial = 1 # initialize
i = 1 # counter
while i <= m:
    factorial = factorial*i
    i= i + 1
print('\nfactorial of '+str(m) +' is '+str(factorial))