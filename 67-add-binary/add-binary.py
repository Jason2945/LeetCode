class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Create a var to hold a carry over
        carry_over = 0
        # Add the numbers together
        ab_sum = int(a) + int(b)
        digit_list = [int(digit) for digit in str(ab_sum)]
        # Start at the last index and move to the first
        for index in range(len(digit_list)-1, -1 , -1):
            if carry_over == 1:
                if digit_list[index] == 2:
                    digit_list[index] = 1
                elif digit_list[index] == 1:
                    digit_list[index] = 0
                else :
                    digit_list[index] = 1
                    carry_over = 0
            else :
                if digit_list[index] == 2:
                    digit_list[index] = 0
                    carry_over = 1
        if carry_over == 1:
            digit_list = [1] + digit_list
        binary_value = "".join(str(digits) for digits in digit_list)
        return(binary_value)