class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Check the numbers and see how many does not equal val
        checkNum = 0
        # Run through the whole list starting from index 0
        for index in range(0, len(nums)):
            # If the element at that index does not equal the value, then bring that element toward the front of nums
            # Then increment checkNums by 1
            if nums[index] != val:
                nums[checkNum] = nums[index]
                checkNum += 1
        return checkNum
        