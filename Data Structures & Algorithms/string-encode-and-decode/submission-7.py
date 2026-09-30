class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for word in strs:
            new_str+=str(len(word)) + "|" + word
        return new_str
        #   5|Hello5|World
    def decode(self, s: str) -> List[str]:
        i=0
        result = []
        while i < len(s):
            j = i
            while s[j]!="|":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            result.append(s[i:j])
            i=j
        return result