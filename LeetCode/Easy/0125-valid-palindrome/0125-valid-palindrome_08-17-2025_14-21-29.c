#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

bool isPalindrome(char* s) 
{
    char* s_start;
    char* temp_s;
    int count;

    temp_s = malloc(strlen(s) * sizeof(char) + 1);
    count = 0;
    while (*s)
    {
        if (isalnum(*s) > 0) //if alphanumeric then copy lower
        {
            temp_s[count] = tolower(*s);
            // printf("%c", temp_s[count]);
            count++;
        }
        s++;
    }
    temp_s[count] = '\0';
    printf("\n%s\n", temp_s);
    
    // check from back of string to front against front to back
    int len_temp = strlen(temp_s);
    count = 0;
    while (temp_s[count] != '\0')
    {
        if (temp_s[count] != temp_s[len_temp - count - 1])
            {
                return false;
            }
        count++;
    }
    return true;
}
