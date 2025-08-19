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
        int j = 0;
        while (separator[j])
        {
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
    int count = 1;
    for (size_t i = 1; i < numofwords; i++)
    {
        temp = strtok(NULL, separator_str);
        if (temp == NULL) 
            continue;
        else
        {
            result[count] = malloc((strlen(temp) + 1) * sizeof(char));
            strcpy(result[count], temp);
            count++;
        }
    }    
    result[count] = NULL;

    return result;
}

char** ft_split_by_sep(char* string, char separator)
{
    char** result;
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

    return result;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** splitWordsBySeparator(char** words, int wordsSize, char separator, int* returnSize) 
{
    char** result;
    char** temp;
    int wordcount;
    int i;

    wordcount = 0;
    int capacity = 16;
    result = malloc(sizeof(char*) * capacity);
    for (size_t count = 0; count < wordsSize; count++)
    {
        temp = ft_split_by_sep(words[count], separator);
        
        i = 0;
        while (temp[i] != NULL)
        {
            if (wordcount + 1 >= capacity)
            {
                capacity = capacity * 2;
                result = realloc(result, (sizeof(char*) * capacity));
            }
            result[wordcount] = temp[i];
            wordcount++;
            i++;
        }
        
    }
    result[wordcount] = NULL;
    returnSize[0] = wordcount;

    return result;
}