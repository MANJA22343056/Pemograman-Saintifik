def prosesDaftarPenulis(authors):
    for author in authors:
        print("Nama:", author[0])
        print("Buku:", author[1])
        print("Penerbit:", author[2])
        print("Tahun Terbit:", author[3])
        print("ISSN:", author[4])
        print("Kota:", author[5])
        print()

authorsList = [
    ["Manja", "Buku Hidup Tenang", "Publisher 1", 2025, "ISSN 1", "Parik"],
    ["Okta", "Buku Hidup Bahagia", "Publisher 2", 2025, "ISSN 2", "Parik"],
    ["Fani", "Buku Hidup Damai", "Publisher 3", 2025, "ISSN 3", "Parik"],
]
print("Informasi Penulis:")
prosesDaftarPenulis(authorsList)