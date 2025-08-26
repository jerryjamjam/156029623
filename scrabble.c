#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int points[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int compute_score(string word);

int main(void)
{
    string p1 = get_string("Player 1:\n");
    string p2 = get_string("Player 2:\n");
    for (int i = 0, n = strlen(p1); i < n; i++)
    {
        p1[i] = tolower(p1[i]);
    }
    for (int j = 0, m = strlen(p2); j < m; j++)
    {
        p2[j] = tolower(p2[j]);
    }
    int score1 = compute_score(p1);
    int score2 = compute_score(p2);
    if(score1 > score2)
    {
        printf("Player 1 Wins!\n");
    }
    else if(score1 < score2)
    {
        printf("Player 2 Wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    int sum = 0;
    for(int i = 0, n = strlen(word); i < n; i++)
    {
        if(islower(word[i]))
        sum += points[word[i] - 'a'];
    }
    return sum;
}
