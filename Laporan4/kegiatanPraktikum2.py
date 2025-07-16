# mendefinisikan fungsi untuk mengirim pesan melalui whatsapp
def kirimPesan(noPenerima, pesan, pengirim="Manja"):
    print("Pesan dari:", pengirim)
    print("Pesan untuk :", noPenerima)
    print("Isi Pesan:", pesan)
    print("Pesan Terkirim!")

# pemanggilan fungsi dengan optional argument
noPenerima = "+6282392257373"
pesan = " Hallo, Kamu diterima di PT Okta Berlian"
kirimPesan(noPenerima, pesan)
print("\n")
# pemanggilan fungsi dengan named argument
noPenerima = "+6282392257373"
pesan = "Kamu sudah bisa bekerja besok!"
pengirim = "PT Okta Berlian"
kirimPesan(noPenerima = noPenerima, pesan = pesan, pengirim = pengirim)