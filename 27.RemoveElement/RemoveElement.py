class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums.copy():
            if i ==val:
                nums.remove(i)
        #print(nums)
        return(len(nums))