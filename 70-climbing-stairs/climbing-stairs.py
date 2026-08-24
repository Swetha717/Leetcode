class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        s1=1
        s2=2
        for _ in range(n-2):
            res=s1+s2
            s1=s2
            s2=res
        return s2