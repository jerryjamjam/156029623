#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int a = 50;
    int b = 10;

    printf("a is %i, b is %i\n", a, b);
    //the & in this example is to show that we want to swap the addresses, not the values of the addresses. 
    swap(&a, &b);
    printf("a is %i, b is %i\n", a, b);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
