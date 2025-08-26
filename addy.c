#include <stdio.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = malloc(strlen(s) + 1)
    if (t = NULL)
    {
        return 1;
    }

    for(int i = 0, n = strlen(s); i < n +1; i++)
    {
        t[i] = s[i];
    }

    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("%s\n", s);
    printf("%s\n", t);

    free(t);
    return 0;
}
