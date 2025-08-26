#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    // checks if argc is not 2 (1 being program name, 2 being command line prompt (key))
    if (argc != 2)
    {
        printf("Wrong command #\n");
        return 1;
    }
    // checks if key is 26 characters
    if (strlen(argv[1]) != 26)
    {
        printf("Must be 26 characters\n");
        return 1;
    }
    // checks if the command line prompt is only alphabetical characters
    for (int i = 0, j = strlen(argv[1]); i < j; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Must only contain Alphanumerical\n");
            return 1;
        }
    }
    // creates array "key" then checks and stores each char in array key, then checks for dupes. if
    // key[i] is greater than 1, that means theres a dupe
    int dupecheck[52] = {0};
    for (int i = 0, j = strlen(argv[1]); i < j; i++)
        if (islower(argv[1][i]))
        {
            int index = (argv[1][i]) - 'a';
            dupecheck[index]++;
        }
        else if (isupper(argv[1][i]))
        {
            int index = (argv[1][i]) - 'A' + 26;
            dupecheck[index]++;
        }
    for (int i = 0; i < 52; i++)
        if (dupecheck[i] > 1)
        {
            printf("Duplicate letters found\n");
            return 1;
        }
    string plaintext = get_string("Plaintext: ");
    string key = argv[1];
    for (int i = 0, j = strlen(plaintext); i < j; i++)
        if (isupper(plaintext[i]))
        {
            int position = plaintext[i] - 'A';
            plaintext[i] = toupper(key[position]);
        }
        else if (islower(plaintext[i]))
        {
            int position = plaintext[i] - 'a';
            plaintext[i] = tolower(key[position]);
        }
    printf("ciphertext: %s\n", plaintext);
}
