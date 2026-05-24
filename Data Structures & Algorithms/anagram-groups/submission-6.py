class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for i in strs:
            #we can create an array that keeps track of letter frequency
            arr = [0] * 26
            for c in i: 
                #using ASCII values we can subtract to update an index in our array
                diff = ord(c) - ord('a')
                arr[diff] += 1
            #print(arr)
            #can't use this array as a key but we can do tuples
            key = tuple(arr)
            #if this specific array/tuple is in there already then add the string to our list values
            if key in hashMap:
                hashMap[key].append(i)
            else: 
            #if not, create one
                hashMap[key] = [i]
            #print(hashMap.values())
            #needs to convert back to list since it's a dict object and the problem is expecting list instead
        return list(hashMap.values())



            
        


        
        