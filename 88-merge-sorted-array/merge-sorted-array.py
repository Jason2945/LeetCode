class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Notes: 
        m is the number that needs to be merged from nums1
        n is the number that needs to be combined from nums2
        m+n is greater than and equal to 1
        m or n itself can be 0

        Steps to solving this
        1. Check if m or n is 0. if m is 0, just set nums1 to equal nums2
        2. If n is 0 no need to do anything
        3. Check from the back to the front, this way it will be sorted from smallest to greatest
        """
        # Do the while loop until there is no more number in nums2
        while n > 0:
            # If there are no more values to be moved from nums1, slice the remainder numbers in nums2 to nums1
            if m == 0:
                nums1[:n] = nums2[:n]
                break
            # If nums1 number is greater than nums2 number, put nums1 number at the back and subtract 1 from m
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m = m-1
            # If nums2 number is greater or equal to nums1 number, put nums2 number at the back and subtract 1 from n
            elif nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n = n-1

        