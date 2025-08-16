#include <string.h>

int len_unrepeated_start(char* s) 
{
    int i;
    int j;
    int s_len;
    int s_temp;
    int found;

    found = 0;
    s_len = strlen(s);
    s_temp = s_len;
    if (s_len == 1)
        return (1);
    i = 0;
    while (i < s_temp)
    {
        j = i + 1;
        while (j < s_temp)
        {
            if (s[i] == s[j])
            {
                s_temp = j + 1; //index to len
                found = 1;
                break;
            }
            j++;
        }
        i++;
    }
    //if search through everything but didn't find same then = s_len
    if (found == 0)
        return (i);
    else
        return (i - 1);
}

int lengthOfLongestSubstring(char* s) 
{
    int temp_len;
    int max_len;

    temp_len = 0;
    max_len = 0;
    while (*s)
    {
        temp_len = len_unrepeated_start(s);
        if (temp_len > max_len)
            max_len = temp_len;
        s++;
    }    
    return (max_len);
}