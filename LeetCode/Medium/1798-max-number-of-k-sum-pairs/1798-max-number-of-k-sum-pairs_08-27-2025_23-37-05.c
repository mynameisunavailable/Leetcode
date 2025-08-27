#include <stdlib.h>

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

int list_max(int* nums, int numscount)
{
    int max = INT_MIN;

    for (int i = 0; i < numscount; i++)
    {
        if (nums[i] > max)
            max = nums[i];
    }
    return max;
}

int maxOperations(int* nums, int numsSize, int k)
{
    int max = list_max(nums, numsSize);
    radix_sort_dec_pos(nums, numsSize, max);
    
    int i, j, count, sum;
    i = 0;
    j = numsSize -1;
    count = 0;
    while (i < j)
    {
        sum = nums[i] + nums[j];
        if (sum == k)
        {
            count += 1;
            i += 1;
            j -= 1;
        }
        else if (sum < k)
            i++;
        else
            j--;
    }

    return count;
}
