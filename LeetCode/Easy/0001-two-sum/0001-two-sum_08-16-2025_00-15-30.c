#include <stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) 
{
    int *result = calloc(2, sizeof(int));
    *returnSize = 2;
    int i;
    int j;

    i = 0;
    while (i < numsSize)
    {
        j = i + 1;
        while (j < (numsSize))
        {
            if (nums[i] + nums[j] == target)
            {
                result[0] = i;
                result[1] = j;
                return (result);
            }
            j++;
        }
        i++;
    }
    return (result);
}
