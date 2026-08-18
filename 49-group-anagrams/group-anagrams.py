class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map={}
        for v in strs:
            key=str(sorted(v))
            if key in hash_map:
                hash_map[key].append(v)
            else:
                hash_map[key]=[v]
        return list(hash_map.values())