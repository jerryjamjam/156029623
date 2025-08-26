#include <cs50.h>
#include <stdio.h>

void print_row(int length);

int main(void)
{
    int height =  get_int("Height: ");

    for (int i = 0; i < height; i++)
    {
        print_row(i + 1);
    }
}

void print_row(int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
    {
        printf("\n");
    }
}


//is the example we based our function off of
void print_row(int spaces, int bricks)
{
    //print row of bricks
}
// you can add anther variable to the function above such as adding int spaces,
