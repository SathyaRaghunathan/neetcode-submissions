class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] +=1
            hm[tuple(count)].append(word)
        
        result =[]
        for val in hm.values():
            result.append(val)
        return result