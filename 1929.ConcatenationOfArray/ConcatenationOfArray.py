class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = nums
        for i in nums.copy():
            res.append(i)
        return(res)

        