class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1

        count = 0
        for i in nums_dict:
            temp = k - i
            if i == temp:
                count += nums_dict[i] // 2
            elif nums_dict.get(i, 0) > 0 and nums_dict.get(temp, 0) > 0:
                min_n = min(nums_dict[i], nums_dict[temp])
                nums_dict[i] = nums_dict[temp] = 0
                count += min_n
            
        return count
