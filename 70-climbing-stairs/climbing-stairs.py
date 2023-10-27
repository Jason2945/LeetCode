class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = 0
        num2 = 0
        numSum = 0
        for counter in range(n + 1):
            if counter == 1:
                num1 = 1
                num2 = 0
            else :
                num2 = num1
                num1 = numSum
            numSum = num1 + num2
        return numSum
        