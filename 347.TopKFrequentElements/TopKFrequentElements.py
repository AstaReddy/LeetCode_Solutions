class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        ans = []
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        sorted_result = dict(sorted(result.items(),key = lambda x : x[1],reverse = True))
        for key in sorted_result.keys():
            if len(ans)>k-1:
                return ans
            else:
                ans.append(key)
        return(ans)


        