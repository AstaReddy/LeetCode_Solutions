class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        count = 0
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i==stack[-1]:
                if count<1:
                    stack.append(i)
                    count+=1
            else:
                stack.append(i)
                count=0
        return("".join(stack))

        