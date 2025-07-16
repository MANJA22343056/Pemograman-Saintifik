def cekDigitBelakang(a, b, c):
    # ambil digit paling kanan dari setiap parameter
    digitA = a % 10
    digitB = b % 10
    digitC = c % 10
    
    # periksa apakah minimal dua dari tiga parameter memiliki
    # digit paling kanan yang sama
    if digitA == digitB or digitA == digitC or digitB == digitC:
        return True 
    else:
        return False 

# cek test-case
print("Input = 30, 20, 18. Output yang diharapkan=", cekDigitBelakang(30, 20, 28))
print("Input = 145, 5, 100. Output yang diharapkan=", cekDigitBelakang(145, 5, 100))
print("Input = 71, 187, 18. Output yang diharapkan=", cekDigitBelakang(71, 187, 18))
print("Input = 1024, 14, 94. Output yang diharapkan=", cekDigitBelakang(1024, 14, 94))
print("Input = 53, 8900, 658. Output yang diharapkan=", cekDigitBelakang(53, 8900, 658))