class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms, hmt = {},{}
        for char in s:
            hms[char] = 1 + hms.get(char,0)
        for char in t:
            hmt[char] = 1 + hmt.get(char,0)
        return hms == hmt