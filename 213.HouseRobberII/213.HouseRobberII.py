class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(arr):
            n = len(arr)
            if n == 0: return 0
            if n == 1: return arr[0]
            first = arr[0]
            curmax = max(arr[0], arr[1])
            for i in range(2, n):
                curmax, first = max(first + arr[i], curmax), curmax
            return curmax

        n = len(nums)
        if n == 1:
            return nums[0]
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
