class Solution:
    def climbStairs(self, n: int) -> int:
        # Make a counter
        counting_up = 0
        # Value for how many ways to count upwards
        num_of_ways = 0
        # Dummy holder 1
        num1 = 0
        # Dummy holder 2
        num2 = 0
        # Keep running until counter equals to int n
        while counting_up <= n:
            # Initize the value for 1 and 2
            if counting_up == 1:
                num1 = 1
                num2 = 0
            elif counting_up == 2:
                num2 = num1
                num1 = 1 
            # Use Fibonacci Sequence to calculate the rest of the steps
            else :
                num2 = num1
                num1 = num_of_ways
            num_of_ways = num1 + num2
            counting_up += 1
        # Return the number of ways to climb the stairs
        return num_of_ways
