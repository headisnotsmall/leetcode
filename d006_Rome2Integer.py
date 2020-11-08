'''

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        RMWD = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        for i in s:
            if i == 'I':
                ans += 1
            elif i == 'V':
                ans += 5
            elif i == 'X':
                ans += 10
            elif i == 'L':
                ans += 50
            elif i == 'C':
                ans += 100
            elif i == 'D':
                ans += 500
            elif i == 'M':
                ans += 1000
        if 'IV' in s:
            ans -= 2
        if 'IX' in s:
            ans -= 2
        if 'XL' in s:
            ans -= 20
        if 'XC' in s:
            ans -= 20
        if 'CD' in s:
            ans -= 200
        if 'CM' in s:
            ans -= 200
        return ans