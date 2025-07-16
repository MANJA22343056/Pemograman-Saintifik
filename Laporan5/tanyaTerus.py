jawab = 'ya'
hitung = 0

while(jawab == 'ya'):
    hitung += 1
    print("Proses %d"%hitung)
    jawab = input("Ulang lagi tidak? ")
    
print("Total perulangan: "+str(hitung))