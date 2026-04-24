class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        r = 0
        m = 0
        for i in range(0,len(nums)):
            for i in range(0, len(nums) - 1):
                if nums[i+1] == nums[i]+1:
                    r = r + 1
                    m = max(r, m)
                else:
                    r = 0
            return m + 1
        