kalimat = input("Masukkan kalimat: ")

# pisahkan kalimat menjadi kata-kata
kataKalimat = kalimat.split()

# cari kata terpendek dan terpanjang
kataTerpendek = min(kataKalimat, key=len)
kataTerpanjang = max(kataKalimat, key=len)

# output
print("Kata terpendek:", kataTerpendek)
print("Kata terpanjang:", kataTerpanjang)