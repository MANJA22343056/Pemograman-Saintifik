data = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VII": "S007"}]

print("data asli: ", data)
nilaiUnik = set( val for dic in data for val in dic.values())
print("nilai uni: ", nilaiUnik)