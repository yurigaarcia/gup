#include <stdio.h>

int main() {

    int INDICE = 13, SOMA = 0, K = 0;

    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }

    printf("A soma dos numeros inteiros de 1 a 13 e: %d", SOMA);

    return 0;
}
