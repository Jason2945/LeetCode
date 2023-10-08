class Solution:
    def isValid(self, s: str) -> bool:
        completed_bracket = ["[]", "{}", "()"]
        s_changed = True
        while s_changed:
            for bracks in completed_bracket:
                if bracks in s:
                    s = s.replace(bracks, "")
                    s_changed = True
                    break
                else :
                    s_changed = False
        if s == "":
            return True
        else :
             False
        