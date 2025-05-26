class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        length = 0

        for word in list(word_count.keys()):
            rev = word[::-1]
            if word != rev:
                if rev in word_count:
                    pair = min(word_count[word],word_count[rev])
                    length += 4 * pair
                    word_count[word] -= pair
                    word_count[rev] -= pair
            else:
                pair = word_count[word] // 2
                length +=  4 * pair
                word_count[word] -= 2 * pair

        for word in word_count:
            if word[0] == word[1] and word_count[word]>0:
                length += 2
                break
        return length
    
        