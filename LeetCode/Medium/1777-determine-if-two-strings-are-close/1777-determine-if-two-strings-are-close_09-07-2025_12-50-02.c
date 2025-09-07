#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

unsigned long long bitmask(char* word)
{
    size_t wordlen = strlen(word);
    unsigned long long u64 = 0;
    for (size_t i = 0; i < wordlen; i++)
    {
        u64 = u64 | (1ULL << (word[i] - 'a'));
    }
    return u64;
}

typedef struct dictcount
{
    char    c;
    int     count;
} dictcount;

//output int* size of 256 * 2, [c, count],[c, count]...
//access c with i * 2 and count with i * 2 + 1
int* count_char(const char* word, size_t* count_char_num)
{
    int length = strlen(word);
    static const int AMOUNT = 256;
    dictcount buckets[AMOUNT];
    int temp_result[AMOUNT * 2];
    int* result;
    
    //initialise buckets as 0
    for (size_t i = 0; i < AMOUNT; i++)
    {
        buckets[i].c = i;
        buckets[i].count = 0;
        // printf("%c: %d\n", buckets[i].c, buckets[i].count);
    }
    
    //count numbers using each bucket
    for (size_t i = 0; i < length; i++)
    {
        buckets[(unsigned char)word[i]].count += 1;
        // printf("%d: %d\n", i, word[i]);
    }
    
    //extract non empty buckets
    size_t res_count = 0;
    for (size_t i = 0; i < AMOUNT; i++)
    {
        if (buckets[i].count > 0)
        {
            temp_result[res_count++] = buckets[i].c;
            temp_result[res_count++] = buckets[i].count;
            // printf("%c: %d\n", buckets[i].c, buckets[i].count); 
            // printf("%c: %d\n", temp_result[i * 2], temp_result[i * 2 + 1]); 
        }
    }

    //copy into the result after assigning the right size
    result = malloc(sizeof(int) * res_count);
    for (size_t i = 0; i < res_count; i++)
    {
        result[i] = temp_result[i];
    }

    count_char_num[0] = res_count;
    return result;
}

bool closeStrings(char* word1, char* word2) 
{
    //check if word1 contains all char in word2 and vice versa
    unsigned long long wordmask1 = bitmask(word1);
    unsigned long long wordmask2 = bitmask(word2);
    if (wordmask1 != wordmask2)
        return false;

    size_t word1_count_num, word2_count_num;
    int* word1_count = count_char(word1, &word1_count_num);
    int* word2_count = count_char(word2, &word2_count_num);
    
    //only check number shape
    for (size_t i = 1; i < word1_count_num; i += 2)
    {
        for (size_t j = 1; j < word2_count_num; j += 2)
        {
            if (word1_count[i] == word2_count[j])
            {
                word1_count[i] = -1;
                word2_count[j] = -1;
                break;
            }
            if ((j == word2_count_num - 1) && word1_count[i] != word2_count[j])
            {
                free(word1_count);
                free(word2_count);
                return false;
            }
        }        
    }

    free(word1_count);
    free(word2_count);
    return true;
}
