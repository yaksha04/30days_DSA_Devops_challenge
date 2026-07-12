class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=0
        maxcount=0
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)
            res= n if count[n]>maxcount else res
            maxcount=max(count[n],maxcount)
        return res    
