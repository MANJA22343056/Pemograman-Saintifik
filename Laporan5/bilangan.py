jumlahBilangan = int(input("Banyak bilangan: \n"))
totalBilangan = 0
rerataBilangan = 0
print("Deret bilangan: ", end='')
for i in range(1,jumlahBilangan+1,1):
    if (i==jumlahBilangan):
        print("%d \n"%i,end='')
    else:
        print("%d + "%i, end='')
    totalBilangan = totalBilangan + i
print("Total seluruh bilangan jika dijumlahkan: %d"%(totalBilangan))
rerataBilangan = totalBilangan/jumlahBilangan
print("Reratanya ialah %d"%(rerataBilangan))