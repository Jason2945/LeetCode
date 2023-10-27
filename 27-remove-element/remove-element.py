class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexPlaceholder = 0
        # Run through all the values
        for index in range(len(nums)):
            # Make sure the number does not equal to the val and move it to the front
            if nums[index] != val:
                nums[indexPlaceholder] = nums[index]
                indexPlaceholder += 1
        return indexPlaceholder
        