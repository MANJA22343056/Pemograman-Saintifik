banyakDonat = int(input("Banyak donat yang ingin dihitung: \n"))
hargaSatuan = int(input("Harga per donat: \n"))
print("Daftar harga donat: ")
for i in range(1,banyakDonat+1,1):
    print("%d donut: \t Rp %d,00"%(i,i*hargaSatuan))