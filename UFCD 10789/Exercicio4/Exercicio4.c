#include <stdio.h>

int main(){

    // Fazer um algoritmo que leia o saldo inicial de cliente do banco e leia também um cheque que entrou e ANALISE
    // se o cheque poderá ser descontado ou não, já que este cliente não possui limite. Se o cheque não poderá ser
    // descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo.

    int saldo, cheque, total;

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
