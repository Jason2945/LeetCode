class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        noDupeIndex = 0
        numsChecked = []
        for index in range(len(nums)):
            if nums[index] not in numsChecked:
                numsChecked.append(nums[index])
                nums[noDupeIndex] = nums[index]
                noDupeIndex += 1
        return noDupeIndex
        