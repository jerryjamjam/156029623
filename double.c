#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size = get_int("What size?: ");
    int sequence[size];

    for (int i = 0; i < size; i++)
    {
        if (i == 0)
        {
            sequence[i] = 1;
        }
        else
        {
            sequence[i] = sequence[i -1] *2;
        }
        printf("%i\n", sequence[i]);
    }
}


