#include <string.h>
#include <stdbool.h>

//only for loweralpha
bool closeStrings(char* word1, char* word2) 
{
    //count number of occurance for each loweralphabet
    size_t word1len = strlen(word1);
    size_t word2len = strlen(word2);
    const size_t AMOUNT = 26; //number of loweralpha
    int word1_count[26] = {0};
    int word2_count[26] = {0};
    
    for (size_t i = 0; i < word1len; i++)
    {
        word1_count[word1[i] - 'a'] += 1;
    }
    for (size_t i = 0; i < word2len; i++)
    {
        word2_count[word2[i] - 'a'] += 1;
    }

    //check if word1 contains all char in word2 and vice versa
    for (size_t i = 0; i < AMOUNT; i++)
    {
        if ((word1_count[i] == 0 && word2_count[i] > 0) || (word2_count[i] == 0 && word1_count[i] > 0))
            return false;
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
