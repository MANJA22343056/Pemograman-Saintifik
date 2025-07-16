# jumlah belanja (dalam rupiah)
belanja = 100000

# besarnya diskon (dalam persen)
diskon = 30

# besarnya diskon
nominalDiskon = (diskon / 100) * belanja

# hitung jumlah yang harus dibayar
# bayar = nominalDiskon - belanja (INI SALAH)

bayar = belanja - nominalDiskon

# tampilkan hasilnya
print("Anda harus membayar: Rp. ", bayar)
