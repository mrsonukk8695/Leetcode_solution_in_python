class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i= 0
        while True:
            for j in range(i+1,len(nums)):
                if nums[i] == target - nums[j]:
                    return [i,j]       
            i+=1
