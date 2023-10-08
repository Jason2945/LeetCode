class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Run the code through all the values in nums
        for index in range(len(nums)):
            # If the value is equal to or greater than the target, return the index as that is where the target's index
            # belong
            if nums[index] >= target:
                return index
        # If the target is larger than every number, it belongs at the end of the list
        return len(nums)
        