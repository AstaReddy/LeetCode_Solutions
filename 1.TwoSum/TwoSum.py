class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in new:
                new[nums[i]] = i
            else:
                return(i,new[diff])
        