int ft_find_num_len(int n)
{
    int count = 0;
    if (n == 0)
        return 1;
    while (n > 0)
    {
        n = n / 10;
        count++;
    }
    return count;
}

#include <math.h>
#include <stdbool.h>
bool isPalindrome(int x) 
{
    int num_len;
    int last_half;
    int first_half;

    if (x < 0)
        return false;    
    num_len = ft_find_num_len(x);
    int last_half_len = num_len / 2;
    last_half = 0;
    for (size_t i = 0; i < last_half_len; i++)
    {
        last_half = (last_half * 10) + (x % 10);
        x /= 10;
    }
    if (ft_find_num_len(x) - 1 == last_half_len)
    {
        x /= 10;
    }
    if (x - last_half == 0)
        return true;
    return false;
}
