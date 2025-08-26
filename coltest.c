#include <cs50.h>
#include <stdio.h>

int coltest(int n);

int main (void)
{
    int n;
    do
    {
        n = get_int("n: ");
    }
    while (n < 0);
    printf("%i\n", coltest(n));
}
int coltest(int n)
{
    if(n == 1)
    {
    return 0;
    }
    else if ((n % 2) == 0)
    {
        return 1 + coltest (n / 2);
    }
    else
    {
        return 1 + coltest (3 * n + 1);
    }
}
