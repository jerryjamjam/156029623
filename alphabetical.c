#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string phrase = get_string("What is the phrase?: ");
    int length = strlen(phrase);
    for (int i = 0; i < length - 1; i++)
    {
        if (phrase[i] > phrase[i + i])
        {
             printf("Error\n");
             return 0;
        }
    }
    printf("YAY\n");
    return 0;
}
