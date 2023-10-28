class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print('testing')
        for index in range(len(nums)):
            if (nums[index] == target):
                return index
            elif (nums[index] > target):
                return index
            # Check if it is the last element in the list
            if (index == len(nums) - 1):
                return index + 1
            

        