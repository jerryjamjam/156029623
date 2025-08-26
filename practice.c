#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

//This is a bogus problem that isnt practical
//Here we allocate space in memory for 3 ints, but decide we want to add more
//so we 'fix it' by adding a temp variable with enough space for 4 ints and
//copy list to tmp.

//not practical at all, but good to understand.
int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if(list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    int *tmp = malloc(4 * sizeof(int));\
    if(tmp == NULL)
    {
        free(list);
        return 1;
    }

    for(int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }
    tmp[3] = 4;

    free(list);
    list = tmp;

    for(int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);
    return 1;
}



(*n).number = 1;   *is the same as*   n - > number = 1;


