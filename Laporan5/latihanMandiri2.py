bilangan = []
inputan = ""
while inputan != "stop":
    inputan = input("Masukkan sebuah bilangan (atau ketik 'stop' untuk berhenti): ")
    if inputan.isdigit():
        bilangan.append(int(inputan))

if bilangan:
    terbesar = max(bilangan)
    terkecil = min(bilangan)
    print("Bilangan terbesar: ", terbesar)
    print("Bilangan terkecil: ", terkecil)
else:
    print("Tidak ada bilangan yang dimasukkan.")