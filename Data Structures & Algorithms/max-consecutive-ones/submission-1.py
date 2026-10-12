class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_couner = 0
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(i,n):
                if nums[j] == 0:
                    break
                count+=1
            max_couner = max(max_couner,count)

        return (max_couner)



        