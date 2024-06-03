class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ll=[]
        for i in nums:
            if i!=val:
                ll.append(i)
        
        for j in range(len(ll)):
            nums[j]=ll[j]
        
        return len(ll)
        
