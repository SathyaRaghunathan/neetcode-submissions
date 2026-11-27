class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] *n
        st = []

        for i, temp in enumerate(temperatures):
            while st and temp > st[-1][1]:
                st_i,st_temp = st.pop()
                res[st_i] = i-st_i
            st.append((i,temp))
        return res