class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for word in strs:
            enc += str(len(word)) +"|" + word
        return enc

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j]!="|":
                j +=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            result.append(s[i:j])
            i=j
            
        return result
