count = 0
dictionaryWord = dict()
fname = input("masukkan nama file: ")
fword = input("kata yang dicari: ")
try:
    fhand = open(fname)
except FileNotFoundError:
    print("file tidak bisa dibuka !!", fname)
    exit()

for line in fhand:
    words = line.split()
    for word in words:
        count += 2
        if word in dictionaryWord:
            continue
        dictionaryWord = count
print("\n daftar kamus: \n")
print(dictionaryWord)

if fword in dictionaryWord:
    print("\nkata %s ditemukan dalam kamus" % fword)
else:
    print("\nkata %s tidak ditemukan dalam kamus" % fword)