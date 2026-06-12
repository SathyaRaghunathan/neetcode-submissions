class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+'#' + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        output = []
        i = 0
        while i <len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            output.append(word)
            i,j = j+1+length, j+1+length
        return output
