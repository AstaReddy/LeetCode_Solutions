class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = -1
        for i in range(len(arr)-1,-1,-1):
            curmax = max(rightmax,arr[i])
            arr[i] = rightmax
            rightmax = curmax
        return arr