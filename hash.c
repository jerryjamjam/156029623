#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>

#define MAX_NAME 256
#define TABLE_SIZE 10

typedef struct
{
    char name[MAX_NAME];
    int age;
} person;

person *hash_table[TABLE_SIZE];

unsigned int hash(char *name)
{
    int length = strlen(name);
    unsigned int hash_value = 0;
    for(int i = 0; i < MAX_NAME; i++)
    {
       hash_value += name[i];
       hash_value = hash_value * name[i] % TABLE_SIZE;
    }
    return hash_value;
}
void init_hash_table()
{
    for(int i = 0; i < TABLE_SIZE; i++)
    {
        hash_table[i] = NULL;
    }
}

void print_table()
{
    for(int i = 0; i < TABLE_SIZE; i++)
    {
        if(hash_table[i] == NULL)
        {
            printf("\t%i\t---");
            else
            {
                printf("\t%i\t%s\n", hash_table[i]->name);
            }
        }
    }
}

int main()
{
    printf("jacob => %u\n", hash("jacob"));
    printf("mary => %u\n", hash("mary"));
    printf("pan => %u\n", hash("pan"));
    printf("jim => %u\n", hash("jim"));
    printf("tim => %u\n", hash("tim"));
    printf("brad => %u\n", hash("brad"));
    return 0;
}
