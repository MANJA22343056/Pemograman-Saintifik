pembelian = int(input("Masukkan total pembelian:"))

if pembelian > 1000000:
    diskon = 0.3 
elif pembelian > 500000 and pembelian <= 1000000:
    diskon = 0.2
elif pembelian >= 1000000 and pembelian <= 500000:
    diskon = 0.15
else:
    diskon = 0
    
total = pembelian * diskon

print("Total pembelian setelah diskon:", total)