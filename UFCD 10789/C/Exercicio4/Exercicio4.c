// Fazer um algoritmo que leia o saldo inicial de cliente do banco e leia tambem um cheque que entrou e ANALISE
// se o cheque podera ser descontado ou nao, ja que este cliente nao possui limite. Se o cheque nao podera ser
// descontado, mostre essa informacao, caso contrario, desconte o cheque e informe o saldo.

#include <stdio.h>

int main(){

    int saldo = 0;
    int cheque = 0;
    int total = 0;

    printf("Insira o seu saldo: ");
    scanf("%d", &saldo);

    printf("Insira o valor do cheque: ");
    scanf("%d", &cheque);

    if(cheque<=saldo){
        total = saldo - cheque;
        printf("\nValor descontado: %d", total);
    } else{
        printf("\nSaldo insuficiente.");
    }

    return 0;

}
