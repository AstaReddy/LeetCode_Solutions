class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        final = []
        for i in range(k):
            max_num = max(res,key=res.get)
            final.append(max_num)
            del res[max_num]
        return(final)
            
        