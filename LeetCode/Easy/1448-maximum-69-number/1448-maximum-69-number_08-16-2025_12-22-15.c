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

//only accepts positive
int power_of_pos(int n, int power)
{
    if (power == 0)
        return (1);
    int result = n;
    while (power - 1 > 0)
    {
        result = result * n;
        power--;
    }
    return (result);
}

//create max_num_len worth of 9. eg. 9999
//9999 - 9669 = 330
//find num_len of 330 is 3
//add 3 * 10^(3-1) to num
int maximum69Number(int num) 
{
    int max_num_len;
    int max_nines;

    max_num_len = ft_find_num_len(num);
    max_nines = 0;
    for (int i = 0; i < max_num_len; i++)
    {
        max_nines = max_nines * 10 + 9;
    }
    int difference = max_nines - num;
    if (difference == 0)
        return (num);
    int diff_len = ft_find_num_len(difference);
    difference = 3 * power_of_pos(10, diff_len - 1);
    num = num + difference;
    
    return (num);
}