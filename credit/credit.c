#include <cs50.h>
#include <stdio.h>

long card_number;
int digit;
int counter;
int product;
long total;
long first_two_digits;
long first_digit;
long digit_amount;

int count_digits(long number);

int main(void)
{
    do
    {
        card_number = get_long("Card Number (No Hyphen): ");
        digit_amount = count_digits(card_number);
    }
    while (card_number < 1 || digit_amount < 13 || digit_amount > 16);
    first_two_digits = card_number;
    while (first_two_digits >= 100)
    {
        first_two_digits /= 10;
    }
    first_digit = card_number;
    while (first_digit >= 10)
    {
        first_digit /= 10;
    }

    int sum1 = 0;
    int sum2 = 0;
    counter = 1;
    int original_card_number = card_number;
    while (card_number > 0)
    {
        digit = card_number % 10;
        if (counter % 2 == 0)
        {
            product = digit * 2;
            if (product >= 10)
            {
                sum1 = sum1 + (product % 10) + (product / 10);
            }
            else
            {
                sum1 = sum1 + product;
            }
        }
        else
        {
            sum2 = sum2 + digit;
        }
        card_number = card_number / 10;
        counter = counter +1;
    }
    total = sum1 + sum2;
    if(total % 10 == 0)
    {
        printf("INVALID\n");
        return 0;
    }
    {
    if(first_two_digits == 34 || first_two_digits == 37)
        {
            printf("AMEX\n");
        }
        else if(first_two_digits >= 51 && first_two_digits <= 55)
        {
            printf("MASTERCARD\n");
        }
        else if(first_digit == 4)
        {
            printf("VISA\n");
        }
    }
}

int count_digits(long number)
{
    int count = 0;
    while (number != 0)
    {
        number /= 10;
        count++;
    }
    return count;
}
