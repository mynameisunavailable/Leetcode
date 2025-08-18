class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for i in words:
            temp_list = i.split(separator)
            for j in temp_list:
                result.append(j)
        result = [x for x in result if x != ""]
        return result