#include <stdbool.h>
bool isPowerOfFour(int n) 
{
    if (n == 0)
    {
        return false;
    }
    else if (n == 1)
    {
        return true;
    }
    long four;
    four = 1;
    while (four < (long)n)
    {
        four = four * 4;
        if (four > (long)n)
        {
            return false;
        }
        else if (four == (long)n)
        {
            return true;
        }
    }
    return false;
}