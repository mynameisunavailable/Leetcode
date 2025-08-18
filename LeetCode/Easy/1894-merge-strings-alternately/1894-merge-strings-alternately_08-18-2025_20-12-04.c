#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char * mergeAlternately(char * word1, char * word2)
{
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    char* result;
    int minlen;

    if (len1 <= len2)
        minlen = len1;
    else
        minlen = len2;
    result = malloc((len1 + len2 + 1) * sizeof(char));
    if (result == NULL)
        return NULL;
    int count_res = 0;
    int count_word = 0;
    while (count_word < minlen)
    {
        result[count_res] = word1[count_word];
        count_res++;
        result[count_res] = word2[count_word];
        count_res++;
        count_word++;
    }
    result[count_res] = '\0';
    if (len1 == len2)
        ;
    else if (len1 > len2)
        strcat(result, &(word1[len2]));
    else
        strcat(result, &(word2[len1]));
    printf("%s\n", result);

    return result;
}