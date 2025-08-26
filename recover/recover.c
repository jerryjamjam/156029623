#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("correct usage\n");
        return 1;
    }
    FILE *input_file = fopen(argv[1], "r");
    if(input_file == NULL)
    {
        printf("image cannot be opened\n");
        return 1;
    }

    uint8_t buffer[512];
    int jpg_number = 0;
    char jpg_name[8];

    FILE *current_file = NULL;

    while(fread(buffer, sizeof(buffer), 1, input_file) == 1)
    {
    if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        if(current_file != NULL)
        {
            fclose(current_file);
        }
        sprintf(jpg_name, "%03i.jpg", jpg_number);
        jpg_number++;
        current_file = fopen(jpg_name, "w");
    }
    if(current_file != NULL)
    {
         fwrite(buffer, sizeof(buffer), 1, current_file);
    }
    }
    fclose(input_file);
    if(current_file != NULL)
    {
        fclose(current_file);
    }
}




