# fungsi konversi celcius ke fahrenheit menggunakan lambda
celciusToFahrenheit = lambda c: (9/5) * c + 32

# fungsi konversi celcius ke reamur menggunakan lambda
celciusToReamur = lambda c: 0.8 * c

# cek test-case
celcius = 100
print("Input C=", celcius, "Output F=", celciusToFahrenheit(celcius))

celcius = 80
print("Input C=", celcius, "Output F=", celciusToReamur(celcius))

celcius = 0
print("Input C=", celcius, "Output F=", celciusToFahrenheit(celcius))
