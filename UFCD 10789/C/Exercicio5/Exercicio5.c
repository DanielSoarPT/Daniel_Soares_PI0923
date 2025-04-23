// Ler 3 valores INTEIROS para as variaveis Num1, Num2, Num3. Apresentar os valores dispostos em ordem crescente e decrescente.

#include <stdio.h>

int main(){

    int num1 = 0;
    int num2 = 0;
    int num3 = 0;

    printf("Insira o valor para o num1: ");
    scanf("%d", &num1);
    printf("Insira o valor para o num2: ");
    scanf("%d", &num2);
    printf("Insira o valor para o num3: ");
    scanf("%d", &num3);
    printf("\n");

    printf("Ordem crescente: ");

    if(num1>num2){
        if(num2>num3){
            printf("%d %d %d", num3, num2, num1);
        } else{
            if(num1>num3){
                printf("%d %d %d", num2, num3, num1);
            }
            else{
                    printf("%d %d %d", num2, num1, num3);
            }
        }
    } else{
        if(num2>num3){
            if(num1>num3){
                printf("%d %d %d", num3, num1, num2);
            } else{
                printf("%d %d %d", num1, num3, num2);
            }
        } else{
            printf("%d %d %d", num1, num2, num3);
        }
    }

    printf("\nOrdem decrescente: ");

    if(num1>num2){
        if(num2>num3){
            printf("%d %d %d", num1, num2, num3);
        } else{
            if(num1>num3){
                printf("%d %d %d", num1, num3, num2);
            }
            else{
                    printf("%d %d %d", num3, num1, num2);
            }
        }
    } else{
        if(num2>num3){
            if(num1>num3){
                printf("%d %d %d", num2, num1, num3);
            } else{
                printf("%d %d %d", num2, num3, num1);
            }
        } else{
            printf("%d %d %d", num3, num2, num1);
        }
    }

    return 0;

}
