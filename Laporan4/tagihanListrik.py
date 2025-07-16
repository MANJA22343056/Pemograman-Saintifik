def tagihanListrik(pemakaian, golongan=3):
    bayar = 0
    pemakaian100 = 100 if pemakaian > 100 else pemakaian
    pemakaian100Lebih = pemakaian - pemakaian100
    if golongan == 1:
        bayar = pemakaian100 * 1500 + pemakaian100Lebih * 2000
    elif golongan == 2:
        bayar = pemakaian100 * 2500 + pemakaian100Lebih * 3000
    elif golongan == 3:
        bayar = pemakaian100 * 4000 + pemakaian100Lebih * 5000
    elif golongan == 4:
        bayar = pemakaian100 * 5000 + pemakaian100Lebih * 7000
    return bayar

print(tagihanListrik(130))
print(tagihanListrik(80,4))
print(tagihanListrik(golongan=1, pemakaian=175))
