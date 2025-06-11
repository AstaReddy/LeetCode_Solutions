class Solution:
    def __init__(self):
        self.encodedict = {}

    def encode(self, strs: List[str]) -> str:
        s = ''.join(strs)
        self.encodedict[s] = strs
        return s
    def decode(self, s: str) -> List[str]:
        return(self.encodedict[s])
