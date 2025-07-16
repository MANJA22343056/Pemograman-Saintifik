def kelipatanSembilan(angka):
    if angka % 9 == 0:
        return True
    else:
        return False
    
kelipatanSembilan = lambda angka: angka % 9 == 0
    
print(kelipatanSembilan(81))
print(kelipatanSembilan(2000))  