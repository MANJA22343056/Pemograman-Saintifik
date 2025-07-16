#include <stdio.h>

int main() {
    float totalPembelian, diskon, cashback, uangKembalian;
    
    printf("=====================================\n");
    printf("==========PROGRAM MINIMART===========\n");
    printf("=====================================\n");
    printf("Masukkan total pembelian: Rp. ");
    scanf("%f", &totalPembelian);
    
    // hitung diskon, cashback, dan uang kembalian
    if (totalPembelian <= 75000) {
        diskon = totalPembelian * 0.05;
        cashback = 0;
    } else if (totalPembelian > 75000 && totalPembelian <= 125000) {
        diskon = totalPembelian * 0.15;
        cashback = 0;
    } else {
        diskon = totalPembelian * 0.25;
        cashback = 5000;
    }
    
    uangKembalian = totalPembelian - diskon - cashback;
    
    printf("Diskon: Rp. %.2f\n", diskon);
    printf("Cashback: Rp. %.2f\n", cashback);
    printf("Uang kembalian: Rp. %.2f\n", uangKembalian);
    
    return 0;
}