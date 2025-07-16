#include <stdio.h>

int main() {
    int pilihan;
    float a, b, hasil;
    
    printf("=====================================\n");
    printf("----Programmer: Manja Fani Okavia----\n");
    printf("-----------Nim: 22343056-------------\n");
    printf("=====================================\n");
    printf("=====PROGRAM KALKULATOR SEDERHANA====\n");
    printf("=====================================\n");
    // menampilkan menu utama
    printf("Menu:\n");
    printf("1) Penjumlahan\n");
    printf("2) Pengurangan\n");
    printf("3) Perkalian\n");
    printf("4) Pembagian\n");
    printf("5) Hasil Bagi\n");
    printf("Pilih operasi (1-5): ");
    scanf("%d", &pilihan);

    // meminta input dua buah bilangan
    printf("Masukkan dua bilangan: ");
    scanf("%f %f", &a, &b);

    // melakukan operasi sesuai dengan pilihan
    switch(pilihan) {
        case 1:
            hasil = a + b;
            printf("Hasil penjumlahan: %.2f\n", hasil);
            break;
        case 2:
            hasil = a - b;
            printf("Hasil pengurangan: %.2f\n", hasil);
            break;
        case 3:
            hasil = a * b;
            printf("Hasil perkalian: %.2f\n", hasil);
            break;
        case 4:
            if(b != 0) {
                hasil = a / b;
                printf("Hasil pembagian: %.2f\n", hasil);
            } else {
                printf("Tidak bisa melakukan pembagian dengan nol.\n");
            }
            break;
        case 5:
            if(b != 0) {
                hasil = (int)a / (int)b;
                printf("Hasil bagi: %d\n", (int)hasil);
            } else {
                printf("Tidak bisa melakukan pembagian dengan nol.\n");
            }
            break;
        default:
            printf("Pilihan tidak valid.\n");
    }

    return 0;
}
