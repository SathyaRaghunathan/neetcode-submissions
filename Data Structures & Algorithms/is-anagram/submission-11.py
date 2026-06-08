class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hms = {}
        hmt = {}
        for i in s:
            if i in hms:
                hms[i] +=1
            else:
                hms[i] = 1
        for i in t:
            if i in hmt:
                hmt[i]+=1
            else:
                hmt[i] =1
        for k,v in hms.items():
            if k in hmt:
                hms[k]-=v
                hmt[k]-=v
                if hms[k] < 0 or hmt[k] <0:
                    return False
            else:
                return False 
        return True
        