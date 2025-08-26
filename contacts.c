#include <cs50.h>
#include <stdio.h>
#include <string.h>

   int main(void)
{
    int age;
    string number;

    string first_name  = get_string("what's your first name? ");
    string last_name = get_string("what's your last name? ");
    printf("hello, %s %s\n", first_name, last_name);

    do
    {
        age = get_int("how old are you? ");
    }
    while (age < 1);
    printf("hello, %s, you are %i\n", first_name, age);

    number = get_string("what is your number? " );

    printf("is your number %s?\n", number);
}
