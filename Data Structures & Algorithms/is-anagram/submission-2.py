class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         sNums = {}
         tNums = {}
         for i in s: 
            #check to see if n already in -> increase += 1
            if i in sNums:
                sNums[i] += 1
            else: 
                sNums[i] = 1
        
         for i in t:
            if i in tNums:
                tNums[i] += 1
            else:
                tNums[i] = 1
         return sNums == tNums




        
        