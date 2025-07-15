class Solution:
    def isValid(self, word: str) -> bool:
        is_vowel = False
        is_consonant = False

        if len(word)<3:
            return False

        for c in word:
            if c.isalpha():
                if c.lower() in 'aeiou':
                    is_vowel = True
                else:
                    is_consonant = True
            elif not c.isdigit():
                return False
        return (is_vowel and is_consonant)
        