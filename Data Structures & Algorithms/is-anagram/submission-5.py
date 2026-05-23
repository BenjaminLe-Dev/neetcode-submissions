class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMaps = {}
        tMaps = {}

        for i in s:
            if i in sMaps:
                sMaps[i] += 1
            else:
                sMaps[i] = 1
        
        for i in t:
            if i in tMaps:
                tMaps[i] += 1
            else:
                tMaps[i] = 1

        return sMaps == tMaps


        