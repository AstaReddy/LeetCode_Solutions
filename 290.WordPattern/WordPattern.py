class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new1, new2 = {}, {}
        s = s.split(" ")
        for c1,c2 in zip(s,pattern):
            if (c1 in new1 and new1[c1] != c2) or (c2 in new2 and new2[c2] != c1) or (len(pattern)!=len(s)) :
                return False
            new1[c1]=c2
            new2[c2]=c1
        return True


        