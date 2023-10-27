class Solution:
    def romanToInt(self, s: str) -> int:
        # Make dictionary for values to be subtracted
        romanSubtraction = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900 }
        # Make dictionary for values of the roman numeral
        romanNumeral = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        # Initialize and declare a variable for the sum of the roman numerals
        romanSum = 0
        # Find if the roman numeral has the subtraction letters
        for subtraction in romanSubtraction.keys():
            if (subtraction in s):
                s = s.replace(subtraction, "")
                romanSum += romanSubtraction[subtraction]
        # After subtraction, add the rest of the roman numerals to romanSum
        for letters in s:
            romanSum += romanNumeral[letters]
        return(romanSum)

        