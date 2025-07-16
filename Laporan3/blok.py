nama = input("Masukkan nama mu: ")
password = input("Masukkan password: ")

if nama == 'Marry':
    print("Hello Marry")
    if password == 'swordfish':
        print("Akses diterima...")
    else:
        print("Password salah!")
else:
    print("maaf kamu bukan marry, akses ditolak!")