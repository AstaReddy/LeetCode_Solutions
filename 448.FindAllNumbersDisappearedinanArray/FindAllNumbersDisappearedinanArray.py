class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new = set(nums)
        res = [0]* len(nums)
        final = []
        for i in new:
            res[i-1] = i
        for i in range(len(res)):
            if res[i]==0:
                final.append(i+1)
        return(final)

        