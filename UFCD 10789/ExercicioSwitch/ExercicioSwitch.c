#include <stdio.h>

int main(){

    // Ler para uma variável INTEIRA um número de 1 a 12 e mostrar o nome do mês correspondente.
    // Caso o mês não existir, mostrar essa informação.

    int mes;

    printf("Insira um numero de 1 a 12 para determinar um mes: ");
    scanf("%d", &mes);

    switch(mes){
        case 1:
            printf("\nJaneiro");
            break;
        case 2:
            printf("\nFevereiro");
            break;
        case 3:
            printf("\nMarco");
            break;
        case 4:
            printf("\nAbril");
            break;
        case 5:
            printf("\nMaio");
            break;
        case 6:
            printf("\nJunho");
            break;
        case 7:
            printf("\nJulho");
            break;
        case 8:
            printf("\nAgosto");
            break;
        case 9:
            printf("\nSetembro");
            break;
        case 10:
            printf("\nOutubro");
            break;
        case 11:
            printf("\nNovembro");
            break;
        case 12:
            printf("\nDezembro");
            break;
        default:
            printf("\nEsse mes nao existe!");
            break;
    }

    return 0;

}
