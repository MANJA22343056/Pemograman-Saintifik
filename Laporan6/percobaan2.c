#include <stdio.h>

void main(){
	printf("== Program Pembayaran ==\n");
	int totalBelanja = 0;
	
	printf("Inputkan total belanja: ");
	scanf(" %i", &totalBelanja);
	
	// menggunakan blok percabangan if
	if (totalBelanja > 100000){
		printf("Selamat, anda mendapatkan hadiah!\n");
	}
	
	printf("Terimakasih sudah berbelanja di toko kami\n\n");
}