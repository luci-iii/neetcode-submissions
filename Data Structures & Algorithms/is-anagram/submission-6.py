class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):

            freq1 = {}
            freq2 = {}

            for char1 in s:
                if char1 in freq1:
                    freq1[char1] += 1
                else:
                    freq1[char1] = 1
            for char2 in t:
                if char2 in freq2:
                    freq2[char2] += 1
                else:
                    freq2[char2] = 1    

            if freq1 == freq2:
                return True

        return False