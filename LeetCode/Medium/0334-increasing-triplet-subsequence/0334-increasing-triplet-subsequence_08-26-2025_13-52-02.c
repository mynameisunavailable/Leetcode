#include <stdbool.h>
bool increasingTriplet(int* nums, int numsSize)
{
    int n1 = __INT_MAX__;
    int n2 = __INT_MAX__;

    for (size_t i = 0; i < numsSize; i++)
    {
        if (nums[i] <= n1)
            n1 = nums[i];
        else if (nums[i] <= n2)
            n2 = nums[i];
        else
            return true;
    }
    return false;
}