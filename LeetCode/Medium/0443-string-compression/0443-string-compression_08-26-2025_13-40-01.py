def append_count(result: list[str], count: int):
    for i in list(str(count)):
        result.append(i)

def append_result(result: list[str], char: str, count: int):
    result.append(char)
    if count > 1:
        append_count(result, count)

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 1:
            return chars
        
        result = []
        char = chars[0]
        count = 0
        for i in chars:
            if char == i:
                count += 1
            else:
                append_result(result, char, count)
                char = i
                count = 1
        append_result(result, char, count)
        chars[:] = result

        return len(chars)