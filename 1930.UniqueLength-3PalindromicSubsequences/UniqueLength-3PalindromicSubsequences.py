from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        new = defaultdict(list)
        for i, val in enumerate(s):
            new[val].append(i)

        count = 0
        for indices in new.values():
            if len(indices) >= 2:
                first = indices[0]
                last = indices[-1]
                unique_middles = set()
                for j in range(first + 1, last):
                    unique_middles.add(s[j])
                count += len(unique_middles)

        return count