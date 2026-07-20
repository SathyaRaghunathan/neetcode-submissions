class Solution:
    def isPalindrome(self, s: str) -> bool:
        scopy = "".join([char.lower() for char in s if char.isalnum()])
        return scopy == scopy[::-1]
        