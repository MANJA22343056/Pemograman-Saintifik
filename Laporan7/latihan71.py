kata1 = input("Masukkan kata pertama: ").lower() # input kata pertama dan ubah ke huruf kecil
kata2 = input("Masukkan kata kedua: ").lower()   # input kata kedua dan ubah ke huruf kecil

# buat kamus kosong untuk menghitung kemunculan setiap huruf dalam kata pertama
kemunculanKata1 = {}

# isi kamus dengan jumlah kemunculan setiap huruf dalam kata pertama
for huruf in kata1:
    kemunculanKata1 [huruf] = kemunculanKata1 .get(huruf, 0) + 1

# periksa apakah jumlah kemunculan setiap huruf dalam kata kedua sama dengan dalam kata pertama
# jika jumlahnya sama untuk setiap huruf, maka kata kedua adalah anagram dari kata pertama
anagram = True
for huruf in kata2:
    if huruf in kemunculanKata1 :
        kemunculanKata1 [huruf] -= 1
        if kemunculanKata1 [huruf] < 0:
            anagram = False
            break
    else:
        anagram = False
        break

# output
if anagram:
    print("Kedua kata adalah anagram.")
else:
    print("Kedua kata bukan anagram.")