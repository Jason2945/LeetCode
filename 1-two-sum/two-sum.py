class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Go through the array for the first number
        for index in range(len(nums)):
            # Go through the array for the second number
            for secondIndex in range(len(nums)):
                # Make sure the index of the first and second number are not the same
                if (index == secondIndex):
                    continue
                # If they equal the target, then return the indexes
                if (nums[index] + nums[secondIndex] == target):
                    return index, secondIndex