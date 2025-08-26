#include <stdio.h>

int fun(int n);

int main()
{
    printf("%i", fun(4));
    return 0;
}

int fun(int n)
{
    if (n == 0)
    {
        return 1;
    }
    else
    return 7 + fun(n-2);
}
