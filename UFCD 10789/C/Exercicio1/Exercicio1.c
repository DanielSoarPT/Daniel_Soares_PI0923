#include <stdio.h>

int main(){

    // Desenvolva um programa que assuma uma entrada em Segundos e transforme em Horas, Minutos e Segundos.

    int segundos;

    printf("Insira a quantidade de segundos: ");
    scanf("%d", &segundos);

    printf("\nHoras: %d\n", segundos / 3600);
    printf("Minutos: %d\n", segundos / 60);
    printf("Segundos: %d", segundos);

    return 0;
}
