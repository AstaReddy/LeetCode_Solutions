class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        first = nums[0]
        curmax = max(nums[0],nums[1])
        for i in range(2,n):
            curmax, first = max( first + nums[i], curmax ), curmax
        return curmax
        