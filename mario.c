#include <stdio.h>
#include <cs50.h>

void print_row(int num_of_spaces_before, int num_of_bricks_before);

int main(void)
{
    int total_rows;
    do
    {
    total_rows = get_int("Pyramid height: ");
    }
    while (total_rows < 1 || total_rows > 8 );
    for (int current_row = 0; current_row < total_rows; current_row++)
    {
        int num_of_bricks_before = current_row + 1;
        int num_of_spaces_before = total_rows - num_of_bricks_before;
        print_row(num_of_spaces_before, num_of_bricks_before);
    }
}
void print_row(int num_of_spaces_before, int num_of_bricks_before)
{
    for(int space_counter_b = 0; space_counter_b < num_of_spaces_before; space_counter_b++)
    {
        printf(" ");
    }
    for(int brick_counter_b = 0; brick_counter_b < num_of_bricks_before; brick_counter_b++)
    {
        printf("#");
    }
    for(int space_counter_a = 0; space_counter_a < 2; space_counter_a++)
    {
        printf(" ");
    }
    for(int brick_counter_a = 0; brick_counter_a < num_of_bricks_before; brick_counter_a++)
    {
        printf("#");
    }
    printf("\n");
}
