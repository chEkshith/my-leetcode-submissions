class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for k in freq:
            if freq[k]>n//2:
                return k
