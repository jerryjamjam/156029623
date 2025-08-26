#include <cs50.h>
#include <stdio.h>
#define QUARTER 25
#define DIME 10
#define NICKLE 5
#define PENNY 1

int main(void)
{
    int coins;
    do
    {
    coins = get_int("Change due: ");
    }
    while (coins < 1);
    int quarters = coins / QUARTER;
    int remaining_q = coins % QUARTER;
    int dimes = remaining_q / DIME;
    int remaining_d = remaining_q % DIME;
    int nickles = remaining_d / NICKLE;
    int remaining_n = remaining_d % NICKLE;
    int pennies = remaining_n / PENNY;
    int remaining_p = remaining_n / PENNY;
    printf("%i\n", quarters + dimes + nickles + pennies);
}
