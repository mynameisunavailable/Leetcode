#include <string.h>
#include <stdio.h>
char* longestCommonPrefix(char** strs, int strsSize) 
{
    char *result;
    int j;

    if (strsSize == 0)
        return "";
    result = malloc(sizeof(char) * strlen(strs[0]) + 1);
    int count = 0;
    result[count] = '\0';
    // printf("result: %s \n", result);
    j = 0;
    while (*(strs[0]))
    {
        // printf("%c: \n", *(strs[0]));
        for (size_t i = 1; i < strsSize; i++)
        {
            // printf("%d, %d, %c\n", i, j, strs[i][j]);
            if (*(strs[0]) != strs[i][j] || (strs[i][j] == '\0'))
            {
                // printf("%s ", result);
                return result;
            }
        }
        j++;
        result[count] = *strs[0];
        // printf("*strs[0]: %c \n", *strs[0]);
        strs[0]++;
        count++;
        result[count] = '\0';
        // printf("result: %s \n", result);
    }
    result[count] = '\0';
    // printf("%s ", result);
    return result;
}