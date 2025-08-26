#include <cs50.h>
#include <stdio.h>
#include <stdint.h>


int main(int argc, char *argv[])
{
    FILE *src = fopen(argv[1], "a");
    if(src == NULL)
    {
        printf("could not open file");
        return 1;
    }

    
    int tests[4];
    char test_name[10];

    for(int i = 0; i < 4; i++)
    {
        int score = get_int("Score? \n");
        sprintf(test_name, "%04i.test", i);
        fprintf(src, "Test: %s, score: %i\n", test_name, score);
    }
     fclose(src);
}
