class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hms = defaultdict(int)
        hmt = defaultdict(int)
        for char in s:
            hms[char] = 1+hms.get(char,0)
        for char in t:
            hmt[char] = 1+ hmt.get(char,0)
        return hms == hmt
        