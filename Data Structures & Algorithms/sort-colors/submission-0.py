class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        m=0
        n=len(nums)-1
        while(m<=n):
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l=l+1
                m=m+1
            elif nums[m]==1:
                m=m+1
            else:
                nums[m],nums[n]=nums[n],nums[m]
                n=n-1
        return nums
        