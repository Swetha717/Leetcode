class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robber(nums):
            r1=0
            r2=0
            for r in nums[::-1]:
                res=max(r+r2,r1)
                r2=r1
                r1=res
            return r1
        return max(robber(nums[1:]),robber(nums[:-1]))
        