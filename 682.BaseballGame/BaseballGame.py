class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in operations:
            if i=='C':
                res.pop()
            elif i=='D':
                res.append(int(res[-1])*2)
            elif i=='+':
                res.append(int(res[-1])+int(res[-2]))
            else:
                res.append(int(i))
        return(sum(res))