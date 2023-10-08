class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueValueIndexHolder = 1
        # Go through the indexes from the second value in num to the last. Skip the first because it can't be a dupe
        for index in range(1, len(nums)):
            # If the value of nums in the previous value does not match the current value move the value forward
            if nums[index - 1] != nums[index]:
                # This will move the new unique num to where the previous duplicate value location was
                nums[uniqueValueIndexHolder] = nums[index]
                # Move up the index for the next unique number as well as tell us how many unique numbers there are
                uniqueValueIndexHolder += 1
        return uniqueValueIndexHolder


        