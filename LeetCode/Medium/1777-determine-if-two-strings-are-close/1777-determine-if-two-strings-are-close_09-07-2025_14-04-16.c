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

//only for loweralpha
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

    for (size_t i = 0; i < word1len; i++)
    {
        word1_count[word1[i] - 'a'] += 1;
        word2_count[word2[i] - 'a'] += 1;
    }
    
    //block out all occurred num
    for (size_t i = 0; i < AMOUNT; i++)
    {
        for (size_t j = 0; j < AMOUNT; j++)
        {
            if (word1_count[i] == word2_count[j])
            {
                word1_count[i] = -1;
                word2_count[j] = -1;
                break;
            }
        }
    }

    //check if there's any unoccurred num
    for (size_t i = 0; i < AMOUNT; i++)
    {
        if (word1_count[i] != -1 || word2_count[i] != -1)
        {
            return false;
        }
    }

    return true;
}
