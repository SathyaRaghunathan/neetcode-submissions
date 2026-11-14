class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = {  "]":"[",   ")":"(",  "}":"{"   }

        for char in s:
            #check if it's a closing bracked
            if char in hm:
                if st and st[-1] == hm[char]:
                    st.pop()
                else:
                    return False
            #if not then append it to the stack
            else:
                st.append(char)
        
        if not st:
            return True
        else:
            return False