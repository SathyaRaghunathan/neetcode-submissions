class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shm = {}
        thm = {}
        for char in s:
            shm[char]= 1+ shm.get(char,0)
        for char in t:
            thm[char] = 1+thm.get(char,0)
        return shm==thm