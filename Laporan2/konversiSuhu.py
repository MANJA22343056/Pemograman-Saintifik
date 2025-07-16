# gunakan lambda untuk mendefinisikan fungsi convertToFahrenheit
convertToFahrenheit = lambda degreesCelsius: degreesCelsius * (9 / 5) + 32

# gunakan lambda untuk mendefinisikan fungsi convertToCelsius
convertToCelsius = lambda degreesFahrenheit: (degreesFahrenheit - 32) * (5 / 9)

# tes dengan assert statements
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

# Kekurangan pembulatan menyebabkan sedikit perbedaan:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
