class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Check the list starting from the end to the beginning
        for index in range(len(digits)-1, -1, -1):
            # If the value is 9, change it to zero
            if digits[index] == 9:
                digits[index] = 0
            # The instant the value is no longer 9, we can add one and return the list
            else :
                digits[index] += 1
                return digits
        # If the number is all 9, add a 1 to the beginning of the list
        return [1] + digits
        