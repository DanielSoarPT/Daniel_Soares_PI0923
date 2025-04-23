// Uma loja oferece para os seus clientes, um determinado desconto de acordo com o valor da compra efetuada.
// O desconto e de 10%, se o valor da compra for ate 200.00€, 15% se for maior que  200€ e menor ou igual a  500,00€ e 20%
// se for acima de 500,00€. Crie um algoritmo que leia o nome do cliente e o valor da compra. Mostre ao final o nome do cliente,
// o valor da compra, o percentual de desconto e o seu valor e valor total a pagar deste cliente. (so fazer duas Contas)

#include <stdio.h>

int main(){

    char nome[50];
    float percentagem = 0;
    float total = 0;
    float compra = 0;

    printf("Insira o seu nome: ");
    scanf("%s", nome);

    printf("Insira o valor da sua compra: ");
    scanf("%f", &compra);

    if(compra<=200){
        percentagem = 0.1;
        total = compra;
        total -= compra * percentagem;
    } else{
        if(compra<=500){
            percentagem = 0.15;
            total = compra;
            total -= compra * percentagem;
        } else{
            percentagem = 0.2;
            total = compra;
            total -= compra * percentagem;
        }
    }

    printf("\nNome do comprador: %s", nome);
    printf("\nValor da compra: %.2f", compra);
    printf("\nDesconto: %.0f porcento", percentagem * 100);
    printf("\nTotal: %.2f", total);

    return 0;

}
