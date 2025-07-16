#kalimat
text ='A quick brown fox jumps over the lazy dog.'

def ambilKataKalimat(kalimat,n):
    kalimat = kalimat.lower() #ubah huruf kecil
    hasilAkhir = []
    hasil = kalimat.split() #pecah berdasarkan spasi
    for i in range (0,len(hasil)): #loop per hasil pecah
        tmp = ' '.join(hasil[i:i+n]) #ambil per indeks
        hasilAkhir.append(tmp) #tambhakan ke list
        
    return hasilAkhir #return

print(ambilKataKalimat(text,2))