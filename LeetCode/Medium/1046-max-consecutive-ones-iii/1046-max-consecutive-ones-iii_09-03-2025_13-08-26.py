#turn nums list into a list of list [number, count]
def conseq_nums_list(nums: list[int]) -> list:
    digit = nums[0]
    digit_count = 0
    conseq_nums = []
    for i in nums:
        if i == digit:
            digit_count += 1
        else:
            conseq_nums.append([digit, digit_count])
            digit = i
            digit_count = 1
    conseq_nums.append([digit, digit_count])
    
    return conseq_nums

#count max conseq one for that segment
def count_conseq_num(conseq_nums: list, k: int, start: int) -> int:
    count = 0
    #add previous substring of 1
    if start - 1 >= 0:
        if conseq_nums[start - 1][0] == 1:
            count += conseq_nums[start - 1][1]
    i = 0
    length = len(conseq_nums)
    while k > 0 and start + i < length:
        if conseq_nums[start + i][0] == 0:
            count += min(k, conseq_nums[start + i][1])
            k -= conseq_nums[start + i][1]
        elif conseq_nums[start + i][0] == 1:
            count += conseq_nums[start + i][1]
        i += 1
    if k == 0 and start + i < length:
        count += conseq_nums[start + i][1]
    
    return count
    
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        conseq_nums = conseq_nums_list(nums)
        #add a first 0 to calc from first 1
        # added = False
        # if conseq_nums[0][0] == 1:
        #     conseq_nums.insert(0,[0, 1])
        #     added = True
        # print(conseq_nums)
        max_count = temp_count = 0
        if k == 0:
            for i in conseq_nums:
                if i[0] == 1:
                    max_count = max(max_count, i[1])
            return max_count

        i = 0
        length = len(conseq_nums)
        while i < length:
            # print(conseq_nums[i])
            # if conseq_nums[i][0] == 0 and i == length - 1:
            if i == length - 1:
                temp_count = count_conseq_num(conseq_nums, k, i)
                max_count = max(max_count, temp_count)
                reversed_conseq_nums = list(reversed(conseq_nums))
                # if added == True:
                #     reversed_conseq_nums.pop(-1)
                temp_count = count_conseq_num(reversed_conseq_nums, k, 0)
                max_count = max(max_count, temp_count)
                break
            elif conseq_nums[i][0] == 0:
                temp_count = count_conseq_num(conseq_nums, k, i)
            max_count = max(max_count, temp_count)
            i += 1

        return max_count