'''

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x2 = ''
        if abs(x) > 2**31:
            return False
        else:
            x1 = str(x)
            for i in range(len(x1)):
                x2 = x1[i] + x2
            if x1 == x2:
                return True
            else:
                return False