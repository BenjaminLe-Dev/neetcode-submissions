class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        # I want to take difference of target - currVal and search hashMap. -> Return both if true.

        # I want to use range(len()) since I want index + value. In this case, the val = key and index = val
        for i in range(len(nums)):
            diff = target - nums[i]
            # if I found the diff in hashmap -> return both
            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[nums[i]] = i