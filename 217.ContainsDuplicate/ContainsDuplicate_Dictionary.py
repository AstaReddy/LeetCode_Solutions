class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        key_value_dict = {}
        for i in nums:
            if i not in key_value_dict:
                key_value_dict[i] = 1
            else:
                key_value_dict[i] += 1
        
        for i in key_value_dict:
            if key_value_dict[i]>1:
                return True
                break
        return False

        