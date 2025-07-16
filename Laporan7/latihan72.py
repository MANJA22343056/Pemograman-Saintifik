kalimat = input("Masukkan kalimat: ")
kataCari = input("Masukkan kata yang ingin dihitung frekuensinya: ")

# hitung frekuensi kemunculan kata yang dicari dalam kalimat
frekuensi = kalimat.lower().count(kataCari.lower())

# output
print(f"Kata '{kataCari}' muncul sebanyak {frekuensi} kali dalam kalimat.")