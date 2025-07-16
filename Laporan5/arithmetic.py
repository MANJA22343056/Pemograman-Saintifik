a = int(input('Enter the first term of the Arithmetic Progression\t: '))
d = int(input('Enter the common difference\t: '))
n = int(input('Enter the number of terms\t: '))

i = 1
sum = 0 #initialize
while i<=n:
    term = a + (i-1) * d
    print('The '+str(i)+'the term is '+str(term))
    sum = sum + term
    i = i + 1
else:
    print('The sum of '+ str(n)+' term is\t: '+ str(sum))