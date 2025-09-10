#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        // vector<int> sorted_nums = nums;
        vector<pair<int, int>> paired_nums;
        for (size_t i = 0; i < nums.size(); i++)
        {
            paired_nums.emplace_back(i, nums[i]);
        }
        sort(paired_nums.begin(), paired_nums.end(), [](pair<int, int>& x, pair<int, int>& y){return x.second < y.second;});
        
        vector<int> result;
        int l = 0;
        int r = paired_nums.size() - 1;
        int sum;

        while (l < r)
        {
            sum = paired_nums[l].second + paired_nums[r].second;
            if (sum > target)
            {
                r--;
            }
            if (sum == target)
            {
                result.push_back(paired_nums[l].first);
                result.push_back(paired_nums[r].first);
                break;
            }
            if (sum < target)
            {
                l++;
            }
        }
        
        return result;
    }
};