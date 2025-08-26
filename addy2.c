#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char *s = get_string("string?: \n");
    char *t = s;

    if(strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
        t[1] = toupper(t[1]);
    }
    printf("%c\n", t[0]);
}

char *t = mallock(strlen(s) + 1);
