def collatz (number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result 

def main():
    while True:
        try:
            inputUser = int(input("Masukkan bilangan bulat: "))
            break
        except ValueError:
            print("Harus memasukkan bilangan bulat!")

    while inputUser != 1:
        inputUser = collatz(inputUser)

if __name__ == "__main__":
    main()