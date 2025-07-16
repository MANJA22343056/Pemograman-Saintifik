def perumtasiTigaAngka(a,b,c):
    return [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]

print("Semua permutasi dari 1, 2, dan 3 adalah:", perumtasiTigaAngka(1, 2, 3))