// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

//global variable from other file
extern int total_words;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 142993;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *checkptr = table[index];
    while(checkptr != NULL)
    {
        if(strcasecmp(word, checkptr->word) == 0)
        {
            return true;
        }
        checkptr = checkptr->next;
    }
    return false;
}
// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    const unsigned int prime = 131071;
    unsigned int hash = 3735928559U;

    for (const char *ptr = word; *ptr; ptr++)
    {
        hash = (hash * prime) + (unsigned char)tolower(*ptr);
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *f = fopen(dictionary, "r");
    if(f == NULL)
    {
        printf("cannot open file\n");
        return false;
    }
    else
    {
        char buffer[LENGTH + 1];
        while(fscanf(f, "%s", buffer) != EOF)
        {
            int bucket = hash(buffer);
            node *n = malloc(sizeof(node));
            if(n == NULL)
            {
                fclose(f);
                return false;
            }

            strcpy(n->word, buffer);

            n->next = table[bucket];
            table[bucket] = n;

            total_words++;
        }
    }
    fclose(f);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return total_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *temp;
    for(int i = 0; i < N; i++)
    {
        node *unptr = table[i];
        while(unptr != NULL)
        {
            temp = unptr;
            unptr = unptr->next;
            free(temp);
        }
    }
    return true;
}



