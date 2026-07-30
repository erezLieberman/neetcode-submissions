class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        flist = [[] for i in range(len(nums)+1)]
        
        for num, count in hashmap.items():
            flist[count].append(num)

        rlist = []

       
        for j in range(len(flist)-1, 0, -1):
            for number in flist[j]:
                rlist.append(number)
                if len(rlist) == k:
                    return rlist

        
        return rlist