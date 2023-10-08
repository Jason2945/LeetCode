class Solution:
    def romanToInt(self, s: str) -> int:
        roman_sub = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
        roman_num = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        Number = 0
        # Do subtraction and leave s with none subtraction
        for key in roman_sub:
            if key in s:
                s = s.replace(key, '')
                Number += roman_sub[key]
        # Add in the other romans into number
        for letter in s:
            Number += roman_num[letter]
        return Number