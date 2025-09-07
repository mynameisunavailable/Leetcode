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

int ft_find_num_len(int n)
{
    int count = 0;
    if (n == 0)
        return 1;
    while (n != 0)
    {
        n = n / 10;
        count++;
    }
    return count;
}

int radix_sort_dec_pos(int* p_nums, int p_numscount, int max)
{
    int digit, c, div;
    int* bucket[10];
    int bucketsize[10] = {0,0,0,0,0,0,0,0,0,0};
    int max_len = ft_find_num_len(max);
    
    if (p_numscount == 0)
        return 0;

    for (int i = 0; i < 10; i++)
    {
        bucket[i] = malloc(p_numscount * sizeof(int));
        if (!bucket[i])
        {
            for (int n = 0; n < i; n++)
                free(bucket[n]);
            return 1; //1 memory failed
        }
    }

    div = 1;
    for (int n = 0; n < max_len; n++)
    {
        //sort by digit size
        for (int i = 0; i < p_numscount; i++)
        {
            digit = (p_nums[i] / div) % 10;
            bucket[digit][bucketsize[digit]] = p_nums[i];
            bucketsize[digit]++;
        }
        //combine back to num list
        c = 0;
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < bucketsize[i]; j++)
            {
                p_nums[c] = bucket[i][j];
                c++;
            }
        }
        div *= 10;
        //reset bucketsize to 0
        for (int i = 0; i < 10; i++)
            bucketsize[i] = 0;        
    }
    
    for (int i = 0; i < 10; i++)
        free(bucket[i]);
    return 0;
}

bool closeStrings(char* word1, char* word2) 
{
    //check if word1 contains all char in word2 and vice versa
    unsigned long long wordmask1 = bitmask(word1);
    unsigned long long wordmask2 = bitmask(word2);
    if (wordmask1 != wordmask2)
        return false;

    //count number of occurance for each loweralphabet
    size_t word1len = strlen(word1);
    size_t word2len = strlen(word2);
    if (word1len != word2len) //if diff length then diff
        return false;

    const size_t AMOUNT = 26; //number of loweralpha
    int word1_count[26] = {0};
    int word2_count[26] = {0};
    int max_count = 0;

    for (size_t i = 0; i < word1len; i++)
    {
        word1_count[word1[i] - 'a'] += 1;
        word2_count[word2[i] - 'a'] += 1;
        if (word1_count[word1[i] - 'a'] > max_count)
            max_count = word1_count[word1[i] - 'a'];
        else if (word2_count[word2[i] - 'a'] > max_count)
            max_count = word2_count[word2[i] - 'a'];
    }

    // for (size_t i = 0; i < AMOUNT; i++)
    // {
    //     printf("%d", word1_count[i]);
    // }
    // printf("\n");
    
    // for (size_t i = 0; i < AMOUNT; i++)
    // {
    //     printf("%d", word2_count[i]);
    // }
    // printf("\n");
    
    radix_sort_dec_pos(word1_count, AMOUNT, max_count);
    radix_sort_dec_pos(word2_count, AMOUNT, max_count);
    
    if (memcmp(word1_count, word2_count, AMOUNT * sizeof(int)) != 0)
        return false;

    return true;
}