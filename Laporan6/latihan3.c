#include <stdio.h>

int main() {
    float nilaiKehadiran, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir;
    
    printf("========================================================\n");
    printf("==============PROGRAM NILAI AKHIR MAHASISWA=============\n");
    printf("========================================================\n");
    printf("Masukkan nilai kehadiran: ");
    scanf("%f", &nilaiKehadiran);
    printf("Masukkan nilai tugas: ");
    scanf("%f", &nilaiTugas);
    printf("Masukkan nilai UTS: ");
    scanf("%f", &nilaiUts);
    printf("Masukkan nilai UAS: ");
    scanf("%f", &nilaiUas);
    
    // hitung nilai akhir
    nilaiAkhir = (nilaiKehadiran * 0.15) + (nilaiTugas * 0.25) + (nilaiUts * 0.25) + (nilaiUas * 0.35);
    
    // tentukan kategori nilai akhir
    char kategori[3];
    if (nilaiAkhir >= 81) {
        strcpy(kategori, "A");
    } else if (nilaiAkhir >= 76) {
        strcpy(kategori, "B");
    } else if (nilaiAkhir >= 66) {
        strcpy(kategori, "C");
    } else if (nilaiAkhir >= 56) {
        strcpy(kategori, "D");
    } else {
        strcpy(kategori, "E");
    }
    
    // cetak nilai akhir dan keterangan hasil kelulusan
    printf("Nilai akhir: %.2f\n", nilaiAkhir);
    
    if (nilaiAkhir >= 81) {
        printf("Selamat! Pertahankan!\n");
    } else if (nilaiAkhir >= 66) {
        printf("Anda lulus, tingkatkan lagi!\n");
    } else if (nilaiAkhir >= 56) {
        printf("Anda lulus, belajar lagi!\n");
    } else {
        printf("Maaf, Anda tidak lulus!\n");
    }
    
    return 0;
}