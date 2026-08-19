class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        res=0
        hash_set=set()
        for j in s:
            while j in hash_set:
                hash_set.remove(s[i])
                i+=1
            hash_set.add(j)
            res=max(res,len(hash_set))
        return res
