#include <stdio.h>

int counter = 0;

int run_me(char* data) {
    counter++;
    for (unsigned int i = 0; i < 2000000; ++i) {
        asm("NOP");
    }
    return counter;
}

int main(void) {
    printf("Hello\n");
    run_me("hi");
    printf("Goodbye\n");
}

