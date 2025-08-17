#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

bool isPalindrome(char* s, int left, int right) 
{
    int count;

    while (left < right)
    {
        if (s[left] != s[right])
            {
                return false;
            }
        left++;
        right--;
    }
    return true;
}

char* longestPalindrome(char* s) 
{
    //check  first char of string (count) to the max len - 1 - count2(0) ispalindrome()
    //if yes then return max len - 1 - count
    //if no then look at string[count] to max_len - 1 - count2(1)
    //check until max_len -1 - count2 == count
    //store max_res
    int count = 0;
    int count2 = 0;
    int max_len = strlen(s);
    size_t max_res = 0;
    char *result;
    char *temp_str;
    size_t len = 0;
    result = malloc(max_len * sizeof(char) + 1);
    temp_str = malloc(max_len * sizeof(char) + 1);
    while (*s)
    {
        if ((size_t)(max_len - 1 - count) < max_res)
            return result;
        count2 = 0;
        
        while (count2 < max_len) 
        {
            strncpy(temp_str, s, max_len - count2);
            temp_str[max_len - count2] = '\0';
            // printf("temp_str: %s\n", temp_str);
            len = strlen(temp_str);
            if (max_res >= len)// early terminate if current max palindrome len is more than remaining
                break;
            if (isPalindrome(temp_str, 0, len - 1) == 1 && max_res < len)
            {
                max_res = len;
                strcpy(result, temp_str);
                result[len] = '\0';
            }
            count2++;
        }
        s++;
        count++;
    }
    free(temp_str);
    return result; 
}