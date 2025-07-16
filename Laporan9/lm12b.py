listData = [1, 2, 3, 4, 5, 1, 2]
setDataFromList = set(listData)
print("List sebelum konversi:", listData)
print("Set setelah konversi dari List:", setDataFromList)

print()

# set menjadi List
setData = {1, 2, 3, 4, 5}
listDataFromSet = list(setData)
print("Set sebelum konversi:", setData)
print("List setelah konversi dari Set:", listDataFromSet)

print()

# tuple menjadi Set
tupleData = (1, 2, 3, 4, 5, 1, 2)
setDataFromTuple= set(tupleData)
print("Tuple sebelum konversi:", tupleData)
print("Set setelah konversi dari Tuple:", setDataFromTuple)

print()

# set menjadi Tuple
setData2 = {1, 2, 3, 4, 5}
tupleDataFromSet = tuple(setData2)
print("Set sebelum konversi:", setData2)
print("Tuple setelah konversi dari Set:", tupleDataFromSet)