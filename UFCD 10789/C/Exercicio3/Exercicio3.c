#include <stdio.h>

int main(){

    // Crie 2 variáveis (num1 e num2) e leia o valor para cada um deles. Mostre os valores de forma crescente e decrescente.

    int num1, num2;

    printf("Insira o primeiro numero: ");
    scanf("%d", &num1);

    printf("Insira o segundo numero: ");
    scanf("%d", &num2);
    printf("\n");

    printf("Ordem crescente: ");

    if(num1>num2){
        printf("%d %d", num2, num1);
    } else{
        printf("%d %d", num1, num2);
    }

    printf("\nOrdem decrescente: ");

    if(num1>num2){
        printf("%d %d", num1, num2);
    } else{
        printf("%d %d", num2, num1);
    }

    return 0;

}
