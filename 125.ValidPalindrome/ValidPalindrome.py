class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return(True)
        new = ""
        for i in s.lower():
            if i.isalnum():
                new+=i
        if new == new[::-1]:
            return(True)
        else:
            return(False)
        