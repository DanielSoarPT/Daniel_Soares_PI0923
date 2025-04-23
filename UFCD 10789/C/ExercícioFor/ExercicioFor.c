// Ler 10 números, e determinar o número par e numero impar….

#include <stdio.h>

int main(){

    int num = 0;

    for(int i = 1; i<=10; i++){
        printf("Insira o numero %d: ", i);
        scanf("%d", &num);
        if(num % 2 == 0){
            printf("\n%d e um numero par.\n\n", num);
        } else {
            printf("\n%d e um numero impar.\n\n", num);
        }
    }

    return 0;

}
