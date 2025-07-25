class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive_list = []
        for i in nums:
            if i > 0:
                positive_list.append(i)
        positive_list = set(positive_list)

        if len(positive_list)==0:
            return max(nums)
        else:
            return sum(positive_list)
        