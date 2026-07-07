class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countst = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            countst[char] = countst.get(char, 0) + 1
        if counts == countst:
            return True
        else:
            return False
        

