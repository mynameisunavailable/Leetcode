def plantflowers(i: int, flowerbed: list[int], n: int, blocked: bool, just_planted: bool) -> bool:
    #stop if all flowers planted
    if n <= 0 and just_planted == False:
        return True
    elif n <= 0 and len(flowerbed) == i:
        return True
    #stop if flowerbed reached the end
    if len(flowerbed) < i + 1:
        return False

    if flowerbed[i] == 1 and just_planted == True:
        flowerbed[i - 1] = 0
        return plantflowers(i + 1, flowerbed, n + 1, True, False)
    elif flowerbed[i] == 1:
        return plantflowers(i + 1, flowerbed, n, True, False)
    elif blocked == True:
        return plantflowers(i + 1, flowerbed, n, False, False)
    elif blocked == False:
        flowerbed[i] = 1
        return plantflowers(i + 1, flowerbed, n - 1, True, True)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return plantflowers(0, flowerbed, n, False, False)