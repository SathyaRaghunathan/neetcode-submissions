class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if self.alpha_num(char):
                newStr += char.lower()
            
        return newStr == newStr[::-1]
        
    def alpha_num(self,char:str)-> bool:
        return (ord('A') <= ord(char)<= ord('Z')
        or ord('a') <=ord(char) <= ord('z')
        or ord('0') <= ord(char) <= ord('9')
        )
        