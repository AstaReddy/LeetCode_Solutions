class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = []
        count = 0
        for i in range(len(nums)):
            if len(res) == 0:
                res.append(nums[i])
            if nums[i] != res[-1]:
                res.append(nums[i])
        print(res)

        for i in range(len(res)):
            l = i-1
            r = i+1
            if l==-1 or r==len(res):
                continue
            elif res[i]<res[l] and res[i]<res[r]:
                count+=1
            elif res[i]>res[l] and res[i]>res[r]:
                count+=1
        return(count)