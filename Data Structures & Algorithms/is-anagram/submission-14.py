class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        l1 = [0] * 26
        for i in range(len(s)):
            l1[ord(s[i])-ord('a')] +=1
            l1[ord(t[i])- ord('a')]-=1
        for val in l1:
            if val >0:
                return False
        return True        