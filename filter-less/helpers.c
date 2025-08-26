#include "helpers.h"
#include <math.h>
#include <stdio.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int average = (int) round((float)(image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalBlue = image[i][j].rgbtBlue;
            int originalGreen = image[i][j].rgbtGreen;

            int newsepiaRed;
            int newsepiaBlue;
            int newsepiaGreen;

            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            newsepiaRed = (sepiaRed > 255) ? 255 : sepiaRed;
            newsepiaBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
            newsepiaGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;

            image[i][j].rgbtRed = newsepiaRed;
            image[i][j].rgbtGreen = newsepiaGreen;
            image[i][j].rgbtBlue = newsepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE tmpa;
            tmpa = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 -j] = tmpa;
        }
    }
    return;
}

// Blur image

void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE new_image[height][width];
    //iterate over i and j because pixels are 2 dimensional
    for(int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            int valid_pixels = 0;
            int sumred = 0;
            int sumblue = 0;
            int sumgreen = 0;
            //iterate over k and j with + and - to check pixels surrounding the current pixel
            for(int k = i - 1; k <= i + 1; k++)
            {
                for(int l = j - 1; l <= j + 1; l++)
                {
                    //check the validity of a surrounding pixel
                    if(k >= 0 && k < height && l >= 0 && l < width)
                    {
                        valid_pixels++;
                        sumred += image[k][l].rgbtRed;
                        sumblue += image[k][l].rgbtBlue;
                        sumgreen += image[k][l].rgbtGreen;
                    }
                }
            }
            new_image[i][j].rgbtRed = round((float)sumred / valid_pixels);
            new_image[i][j].rgbtBlue = round((float)sumblue / valid_pixels);
            new_image[i][j].rgbtGreen = round((float)sumgreen / valid_pixels);
        }
    }
    for(int m = 0; m < height; m++)
    {
        for(int n = 0; n < width; n++)
        {
            image[m][n] = new_image[m][n];
        }
    }
}


