class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        noDupeIndex = 0
        numsChecked = []
        # Run through every item in the list
        for index in range(len(nums)):
            # If the number is not a duplicate, move it to the front of the most unique number
            # Add it to the list of numbers that appeared
            # Increase the counter of the amount of unseen duplicates
            if nums[index] not in numsChecked:
                numsChecked.append(nums[index])
                nums[noDupeIndex] = nums[index]
                noDupeIndex += 1
        return noDupeIndex
        