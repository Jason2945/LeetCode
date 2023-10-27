class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ""
        closing = ['}', ']', ')']
        # Run through the string
        for chars in s:
            # Check to make sure the first character isnt a closing bracket
            if chars in closing:
                if len(openBrackets) < 1:
                    return False
            # Check to see if it is open bracket, if it is add it to a new string
            if (chars == '{' or chars == '[' or chars == '('):
                openBrackets += chars
            # Check to make sure that when closing, the previous one matches
            elif (chars == "}" and openBrackets[-1] != "{"):
                return False
            elif (chars == "]" and openBrackets[-1] != "["):
                return False
            elif (chars == ")" and openBrackets[-1] != "("):
                return False
            # Make sure all opened brackets are closed
            else :
                openBrackets = openBrackets[:-1]
        # Make sure there are nothing left and all brackets are closed
        if openBrackets == "":
            return True
        else :
            return False

        