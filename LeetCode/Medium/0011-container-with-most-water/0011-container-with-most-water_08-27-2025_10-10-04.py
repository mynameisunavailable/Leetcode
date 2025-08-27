def rect_area(height: list[int], h1: int, h2: int):
    h = min(height[h1], height[h2])
    w = h2 - h1
    return h * w

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = max_area = 0
        j = len(height) - 1
        while i < j:
            temp_area = rect_area(height, i, j)
            max_area = max(temp_area, max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            
        return max_area