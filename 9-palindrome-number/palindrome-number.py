class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Change x into a string
        number = str(x)
        # Create a single empty string to check if it is palindrome
        palindrome_check = ""
        # Put the digits in number in reverse to the palindrome check and compare if they are the same
        for dig in reversed(number):
            palindrome_check += dig
        if palindrome_check == number:
            return True
        else:
            return False
