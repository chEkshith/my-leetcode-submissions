class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        wr=0
        for re in range(len(nums)):
            if nums[re]!=0:
                nums[wr]=nums[re]
                wr+=1
        for i in range(wr,len(nums)):
            nums[i]=0
        