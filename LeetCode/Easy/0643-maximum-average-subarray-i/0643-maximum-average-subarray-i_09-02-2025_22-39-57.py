class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        max_res = sum(nums[left: k])
        # print(max_res)
        temp_res = max_res
        while right < len(nums):
            # print(nums[i:i + k])
            # print(left, right)
            max_res = max(temp_res, max_res)
            if right >= len(nums) - 1:
                break
            temp_res = temp_res - nums[left] + nums[right + 1]
            # print(temp_res)
            left += 1
            right += 1
        return max_res / k