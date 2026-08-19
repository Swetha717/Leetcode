class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for n in nums:
            if n==0:
                nums.remove(0)
                nums.append(0)