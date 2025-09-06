#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef struct 
{
    char lower_alpha;
    int count;
} dict;

//output int* size of 26 * 2, [lower_alpha, count],[lower_alpha, count]...
//access lower_alpha with i * 2 and count with i * 2 + 1
int* compress_string(char* word)
{
    int length = strlen(word);
    dict buckets[26];
    int* result = malloc(sizeof(int) * 26 * 2);
    
    for (size_t i = 0; i < 26; i++)
    {
        buckets[i].lower_alpha = i + 'a';
        buckets[i].count = 0;
        // printf("%c: %d\n", buckets[i].lower_alpha, buckets[i].count);
    }
    
    for (size_t i = 0; i < length; i++)
    {
        buckets[word[i] - 'a'].count += 1;
        // printf("%d: %d\n", i, word[i]);
    }
    
    for (size_t i = 0; i < 26 * 2; i += 2)
    {
        result[i] = buckets[i / 2].lower_alpha;
        result[i + 1] = buckets[i / 2].count;
        // printf("%c: %d\n", buckets[i].lower_alpha, buckets[i].count); 
        // printf("%c: %d\n", result[i], result[i+1]); 
    }

    return result;
}

bool closeStrings(char* word1, char* word2) 
{
    int* word1_count = compress_string(word1);
    int* word2_count = compress_string(word2);

    for (size_t i = 0; i < 26; i++)
    {
        if ((word1_count[i * 2 + 1] > 0 && word2_count[i * 2 + 1] == 0) 
        || (word2_count[i * 2 + 1] > 0 && word1_count[i * 2 + 1] == 0))
        {
            free(word1_count);
            free(word2_count);
            return false;
        }
    }
    
    for (size_t i = 0; i < 26; i++)
    {
        for (size_t j = 0; j < 26; j++)
        {
            if (word1_count[i * 2 + 1] == word2_count[j * 2 + 1])
            {
                word1_count[i * 2 + 1] = -1;
                word2_count[j * 2 + 1] = -1;
                break;
            }            
        }        
    }
    
    // for (size_t i = 0; i < 26; i ++)
    // {
    //     // printf("%c: %d\n", buckets[i].lower_alpha, buckets[i].count); 
    //     // printf("%d: %d\n", i * 2, i * 2 + 1); 
    //     printf("%c: %d\n", word1_count[i * 2], word1_count[i * 2 + 1]); 
    //     printf("%c: %d\n", word2_count[i * 2], word2_count[i * 2 + 1]); 
    // }

    for (size_t i = 0; i < 26; i++)
    {
        if (word1_count[i * 2 + 1] != -1 || word2_count[i * 2 + 1] != -1)
        {
            free(word1_count);
            free(word2_count);
            return false;
        }
    }

    free(word1_count);
    free(word2_count);
    return true;
}
