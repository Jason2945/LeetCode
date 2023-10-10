class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_len = m + n
        # Make sure that there is elements in nums2 or else don't do anything
        if n == 0:
            pass
        else :
            # Run through all the values in nums1
            for index in range(total_len):
                # Skip all the elements in m that does not need to be replaced
                if index <= m-1:
                    pass
                # Replace the holder values in nums1 with nums2 elements
                else :
                    nums1[index] = nums2[n-1]
                    # Subtract the number of values that need to be added to nums1
                    n -= 1
            # Sort the number into non-decreasing order
            nums1.sort()
        