'''

Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x1 = str(x)
        x2 = ''
        if abs(x) > 2**31:
            return 0
        else:
            if x1[0] != '-':
                for i in range(len(x1)):
                    x2 = x1[i] + x2
            else:
                for i in range(1, len(x1)):
                    x2 = x1[i] + x2
                x2 = x1[0] + x2
            ans = int(x2)
            if abs(ans) > 2**31-1 :
                return 0
            else:
                return ans


'''

if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2

'''