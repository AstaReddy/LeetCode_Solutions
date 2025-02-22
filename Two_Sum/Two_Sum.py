class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in new_map:
                return [new_map[diff],index]
            new_map[value] = index
        