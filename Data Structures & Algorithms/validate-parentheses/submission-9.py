class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        hm = {  "]":"[",
        ")":"(",
        "}":"{"  }

        for char in s:
            #if closing bracket
            if char in hm:
                if st and st[-1] == hm[char]:
                    st.pop()
                else:
                    return False
            #if open bracket
            else:
                st.append(char)

        if not st:
            return True
        else:
            return False