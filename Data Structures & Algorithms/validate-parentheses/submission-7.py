class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = { "]":"[",
         ")":"(",
        "}":"{" }
        
        for char in s:
            if char in hm:
                if st and st[-1] == hm[char]:
                    st.pop()
                else:
                    return False

            else:
                st.append(char)
        
        if not st:
            return True
        else:
            return False