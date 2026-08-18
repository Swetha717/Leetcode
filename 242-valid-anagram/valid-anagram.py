class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s={}
        hash_map_t={}
        for v in s:
            hash_map_s[v]=hash_map_s.get(v,0)+1
        for v in t:
            hash_map_t[v]=hash_map_t.get(v,0)+1
        return hash_map_s==hash_map_t