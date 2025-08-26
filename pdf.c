#include <cs50.h>
#include <stdio.h>
#include <stdint.h>

int main (int argc, string argv[])
{
    string filename = argv[1];
    FILE *f = fopen(filename, "r");
    //here we're using uint8_t because of it's structure (it's positive, and a certain length.)
    //stands for unassigned, int, 8 bits, and is it's own type.
    uint8_t buffer[4];
    fread(buffer, 1, 4, f)

    for (int i =0; i < 4; i++)
    {
        printf("%i\n". buffer[i]);
    }
    fclose(f);
}

int *px = malloc(sizeof(int));


int arr[10];
fwrite(arr, sizeof(int), 10, ptr);
