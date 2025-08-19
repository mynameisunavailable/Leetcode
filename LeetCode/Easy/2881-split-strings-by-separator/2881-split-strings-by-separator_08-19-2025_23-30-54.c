#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int ft_count_sep(char* string, char* separator)
{
    int count = 0;
    int i = 0;

    int lensep = strlen(separator);
    if (strlen(string) < lensep)
        return -1;
    while (string[i])
    {
        // printf("%c, ", string[i]);
        int j = 0;
        while (separator[j])
        {
            // printf("%c, %c \n", string[i + j], separator[j]);
            if (string[i + j] == separator[j] && (separator[j + 1] == '\0'))
            {
                j++;
                count++;
                i = i + lensep - 1;
            }
            else if (string[i + j] == separator[j])
                j++;
            else
                break;
        }
        i++;
    }
    return count;
}

char** ft_split_by_sep_raw(char* string, char* separator_str, char** result, int numofwords)
{
    char* temp;
    char stringcpy[strlen(string)+1];

    strcpy(stringcpy, string);
    temp = strtok(stringcpy, separator_str);

    result[0] = malloc((strlen(temp) + 1) * sizeof(char));
    strcpy(result[0], temp);
    // printf("temp 0: %s, \n", temp);
    for (size_t i = 1; i < numofwords; i++)
    {
        temp = strtok(NULL, separator_str);
        // printf("temp %d: %s, \n", i, temp);
        if (temp == NULL) 
        {
            result[i] = malloc(1);
            result[i][0] = '\0';
            continue;
        }
        // printf("temp %d: %s, \n", i, temp);
        result[i] = malloc((strlen(temp) + 1) * sizeof(char));
        strcpy(result[i], temp);
    }    
    result[numofwords] = NULL;

    return result;
}

char** ft_split_by_sep(char* string, char separator)
{
    char** result;
    int i;

    //if string is empty then return NULL string
    if (*string == '\0')
    {
        result = malloc(sizeof(char*));
        result[0] = NULL;
        return result; 
    }
    //search through string for number of sep
    char separator_str[2] = {separator, '\0'}; //magic number for char sep
    int num_of_sep = ft_count_sep(string, separator_str);
    //if number of sep == number of char in main string/strlen(separator_str) 
    //in str then return NULL string
    if (num_of_sep == strlen(string) / strlen(separator_str))
    {
        result = malloc(sizeof(char*));
        result[0] = NULL;
        return result; 
    }

    int numofwords = num_of_sep + 1;
    result = malloc((numofwords + 1) * sizeof(char*));
    ft_split_by_sep_raw(string, separator_str, result, numofwords);

    // for (size_t i = 0; result[i] != NULL; i++)
    // {
    //     printf("result[%d] %s, \n", i, result[i]);
    // }
    //remove empty strings
    i = 0;
    int j = 0;
    char** final_result = malloc((numofwords + 1) * sizeof(char*));
    while (result[i] != NULL)
    {
        if (result[i][0] != '\0')
        {
            final_result[j] = result[i];
            j++;
        }
        i++;
    }
    final_result[j] = NULL;
    // for (size_t i = 0; i < numofwords; i++)
    // {
    //     printf("final_result[%d] %s, \n", i, final_result[i]);
    // }
    
    return final_result;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** splitWordsBySeparator(char** words, int wordsSize, char separator, int* returnSize) 
{
    char** result;
    char** temp;
    int wordcount;

    wordcount = 0;
    temp = malloc(sizeof(char*));
    result = malloc(sizeof(char*));
    for (size_t count = 0; count < wordsSize; count++)
    {
        // printf("word %d: %s\n", count, words[count]);
        temp = ft_split_by_sep(words[count], separator); //realloc for more size for each word pointer?
        
        while (*temp != NULL)
        {
            // printf("temp: %s\n", temp[0]);
            result = realloc(result, (wordcount + 2) * sizeof(char*));
            result[wordcount] = temp[0];
            wordcount++;
            temp++;
        }
        
    }
    result[wordcount] = NULL;
    returnSize[0] = wordcount;

    return result;
}