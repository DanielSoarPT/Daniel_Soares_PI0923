#include <stdio.h>

int main(){

    // O sistema de avaliação de determinada disciplina, é composto por três provas Nota (0 a 10).
    // A primeira prova tem peso 2, a Segunda tem peso 3 e a terceira prova tem peso 5.
    // Faça um algoritmo para calcular a média final de um aluno desta disciplina e se a media for maior ou igual a 6, mostrar APROVADO, senão, mostrar REPROVADO.

    float nota1, nota2, nota3, media;

    printf("Insira a nota da primeira prova: ");
    scanf("%f", &nota1);
    printf("Insira a nota da segunda prova: ");
    scanf("%f", &nota2);
    printf("Insira a nota da terceira prova: ");
    scanf("%f", &nota3);

    nota1 == (nota1 * 2) / 10;
    nota2 == (nota2 * 3) / 10;
    nota3 == (nota3 * 5) / 10;
    media = (nota1 + nota2 + nota3) / 3;

    if(media>=6){
        printf("\nMedia: %.2f", media);
        printf("\nAPROVADO!");
    } else{
        printf("\nMedia: %.2f", media);
        printf("\nREPROVADO!");
    }

    return 0;

}
