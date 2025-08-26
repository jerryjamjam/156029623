#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

float side [3];
bool valid_triangle(float x, float y, float z);
// can change the 3 to a const variable
int main(void)
{
for (int i = 0; i < 3; i++)
do
{
    side[i] = get_float("Side %i: ", i+1);
}
while (side[i] <= 0);

bool result = valid_triangle(side[0], side[1], side[2]);
if (result)
{
    printf("Valid\n");
}
else
{
    printf("NotValid\n");
}
}

bool valid_triangle(float x, float y, float z)
{
if ((x + y <= z) || (x + z <= y) || (y + z <= x))
{
return false;
}
else
{
return true;
}
}

int foo[5] = {1, 2, 3, 4, 5};
int bar[5];

for (int i = 0; i < 5; i++)
{
    bar[i] = foo[i];
}



