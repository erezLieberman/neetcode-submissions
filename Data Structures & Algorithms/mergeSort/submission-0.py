# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self,right, left):
        result = []
        i, j = 0,0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        while i < len(left):
            result.append(left[i])
            i+=1

        while j < len(right):
            result.append(right[j])
            j+=1
    
        return result

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])

        return self.merge(right, left)
