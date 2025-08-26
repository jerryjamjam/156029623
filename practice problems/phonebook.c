#include <cs50.h>
#include <stdio.h>
#include <string.h>

#define SIZE 3

// we created a new data type by combining name and number
typedef struct
{
    string name;
    string number;
} person;

int main(void)
{
    person people[SIZE];

    people[0].name = "carter";
    people[0].number= "+1-715-730-0472";

    people[1].name = "david";
    people[1].number = "+1-715-730-0472";

    people[2].name = "john";
    people[2].number = "+1-898-879-8899";

    string name = get_string("name: ");
    for(int i = 0; i < SIZE; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
        printf("Found %s\n", people[i].number);
        return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}
