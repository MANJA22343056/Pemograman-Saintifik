def hitungBelanja (belanja, diskon=0):
    bayar = belanja - ( belanja * diskon)/100
    return bayar

print(hitungBelanja(100000))
print(hitungBelanja(100000, 10))
print(hitungBelanja(100000, 50))