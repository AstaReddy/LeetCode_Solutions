class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        storedict = Counter(nums)
        res = []   
        for i in storedict:
            if storedict[i]>(math.floor(len(nums)/3)):
                res.append(i)
        return(res)
