// Fazer um programa que analise 3 valores inteiros (atrav�s das vari�veis num1, num2 e num3),e informa qual o maior e qual o menor deles

#include <stdio.h>

int main(){

    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    int maior = 0;
    int menor = 0;

    printf("Insira o primeiro numero: ");
    scanf("%d", &num1);

    printf("\nInsira o segundo numero: ");
    scanf("%d", &num2);

    printf("\nInsira o terceiro numero: ");
    scanf("%d", &num3);

    maior = num1;
    menor = num1;

    if(num2>maior){
        maior = num2;
    }

    if(num3>maior){
        maior = num3;
    }

    if(num2<menor){
        menor = num2;
    }

    if(num3<menor){
        menor = num3;
    }

    printf("\nMaior: %d\nMenor: %d", maior, menor);

    return 0;

}
