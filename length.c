#include <cs50.h>
#include <stdio.h>

int string_length(string s);

int main(void)
{
    char *name = get_string("Name: ");
    int length = string_length(name);
    printf("%i\n", length);
}

int string_length(string s)
{
    int n = 0;
    while (s[n] != '\0' )
    {
        n++;
    }
    return n;
}

//this is basically just showing that we created the function
//for string_lenghth, but in reality we can use the <string.h>
//library where a function to turn a string into an int already exists.

int main (void)
{
    char *name = get_string("Name: ");

    int n = 0;
    while (name[n] != '/0')
    {
        n++;
    }
    printf("%i\n", n);
}
