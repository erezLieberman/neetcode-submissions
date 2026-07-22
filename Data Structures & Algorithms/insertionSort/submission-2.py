# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        result = []
        pairs_copy = pairs.copy()
        result.append(pairs.copy())
        for i in range (1, len(pairs_copy)):
            j = i-1
            while j >= 0 and pairs_copy[j].key > pairs_copy[j+1].key:
                temp = pairs_copy[j]
                pairs_copy[j] = pairs_copy[j+1]
                pairs_copy[j+1] = temp
                j-=1
            result.append(pairs_copy.copy())
        return result