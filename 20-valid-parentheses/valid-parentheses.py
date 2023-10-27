class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ""
        closing = ['}', ']', ')']
        for chars in s:
            if chars in closing:
                if len(openBrackets) < 1:
                    return False
            if (chars == '{' or chars == '[' or chars == '('):
                openBrackets += chars
            elif (chars == "}" and openBrackets[-1] != "{"):
                return False
            elif (chars == "]" and openBrackets[-1] != "["):
                return False
            elif (chars == ")" and openBrackets[-1] != "("):
                return False
            else :
                openBrackets = openBrackets[:-1]
        if openBrackets == "":
            return True
        else :
            return False

        