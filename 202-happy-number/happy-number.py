class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set=set()
        while True:
            if n==1:
                return True
            if n in hash_set:
                return False
            hash_set.add(n)
            s=0
            for v in str(n):
                s+=int(v)**2
            n=s
