class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        # print(nums_dict)

        count = 0
        for i in nums:
            temp = k - i
            if nums_dict.get(temp) is not None and nums_dict[temp] > 0 and nums_dict[i] > 0:
                if i == temp and nums_dict[temp] < 2:
                    pass
                else:
                    nums_dict[temp] -= 1
                    count += 1
            nums_dict[i] -= 1

        return count