def uniqueSum (list):
    dataSet = set(list)
    
    total = 0
    for data in dataSet:
        total = total + data
        
    return total
contoh1 = [2,4,3,2,7,8,6,4,5,5]
hasil1 = uniqueSum(contoh1)
print(hasil1)