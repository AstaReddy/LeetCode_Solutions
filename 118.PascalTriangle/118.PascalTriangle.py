class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  

        for i in range(numRows - 1):  
            prev_row = res[-1]
            temp = [0] + prev_row + [0]  
            row = []

            for j in range(len(prev_row) + 1):
                row.append(temp[j] + temp[j + 1])  

            res.append(row)  

        return res
