class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                key[index] +=1
            key = tuple(key)
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return list(hashmap.values())
    