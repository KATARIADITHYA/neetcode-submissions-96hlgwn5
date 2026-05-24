class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        r=set()
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>(n/3):
                r.add(i)
        return list(r)
        