def temukanFaktor(angka):
    faktor = []
    for i in range(1, angka + 1):
        if angka % i == 0:
            faktor.append(i)
    return faktor

print("Faktor-faktor dari 30:", temukanFaktor(30))