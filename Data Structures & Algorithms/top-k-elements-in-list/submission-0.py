class Solution:
    def topKFrequent(self, nums: int, k: int) -> List[int]:
        
        hashMap = {}
        #At each index, I want a list of values.
        #I know that max frequency would be the length of nums so make that many buckets
        bucket = [[] for i in range(len(nums)+1)]
        answer = []

        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        #Take frequency (values) and add key to index

        for i in hashMap:
            #Frequency = Index. Thus bucket[values].append(key)
            bucket[hashMap[i]].append(i)

        for i in range(len(bucket)-1, 0, -1):
            if i:
                answer.extend(bucket[i])
            if len(answer) == k:
                return answer

        

            
        
        
        print(bucket)