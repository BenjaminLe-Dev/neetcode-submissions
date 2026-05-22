class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxim = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > maxim:
                    maxim = counter
                counter = 0
        if counter > maxim:
            maxim = counter
        return maxim

        