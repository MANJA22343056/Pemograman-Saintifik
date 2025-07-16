def cekAngka(a, b, c):
    # mengecek apakah ketiga parameter berbeda semua
    if a != b and a != c and b != c:
        # mengecek adakah ada kemungkinan jika diambil dua parameter
        # dan dijumlahkan hasilnya sama dg parameter lainnya
        if a + b == c or a + c == b or b + c == a:
            return True
    return False

# panggil fungsi
print(cekAngka(4,5,9))
print(cekAngka(4,5,10))
print(cekAngka(7,3,10))