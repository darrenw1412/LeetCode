class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        total = 0

        for i in range(len(s) - 1):
            if roman_number[s[i]] < roman_number[s[i + 1]]:
                total -= roman_number[s[i]]
            else:
                total += roman_number[s[i]]

        total += roman_number[s[-1]]
        return total
        