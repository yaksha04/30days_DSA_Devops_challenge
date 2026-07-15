class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            mn=nums[i]
            ind=i
            for j in range(i+1,n):
                if nums[j]<mn:
                    mn=nums[j]
                    ind=j
            nums[i],nums[ind]=nums[ind],nums[i]
        return nums            
