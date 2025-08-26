#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    string input = get_string("What is your input? \n");

    int sentencecount = 0;
    for(int i = 0, j = strlen(input); i < j; i++ )
    {
        if(input[i] == '.' || input[i] == '!' || input[i] == '?')
        {
            sentencecount++;
        }
    }

    int wordcount = 0;
    bool ifword = false;
    for (int i = 0; input[i] != '\0'; i++ )
    {
         if(isspace(input[i]))
        {
            ifword = false;
        }
        else if(ifword == false)
        {
            wordcount++;
            ifword = true;
        }
    }

    int charcount = 0;
    bool ifchar = false;
    for (int i = 0; input[i] != '\0'; i++ )
    {
         if(isalpha(input[i]))
        {
            ifchar = true;
            charcount++;
        }
    }

    float l = (float)charcount / wordcount * 100;
    float s = (float)sentencecount / wordcount * 100;
    float index = .0588 * l - 0.296 * s - 15.8;
    int rounded_index = round(index);
    printf("Grade %i\n", rounded_index);
}
