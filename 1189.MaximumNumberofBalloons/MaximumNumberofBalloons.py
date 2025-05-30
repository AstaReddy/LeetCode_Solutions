class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        test = Counter("balloon")
        print(countText)
        print(test)
        res = len(text)

        for c in test:
            res = min(res,countText[c]//test[c])
        return(res)
        