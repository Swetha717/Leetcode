class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums.pop(i)
                nums.insert(j,temp)
                j+=1
        return nums