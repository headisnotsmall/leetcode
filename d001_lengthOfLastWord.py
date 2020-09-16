class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()
        if len(word) != 0:
            return word, (len(word[-1]))
        else:
            return word, 0

s = input("insert a str")
a = Solution.lengthOfLastWord("a", s)
print(a)

# str.split() can split words with "" or " " or "\n"

'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = s.split()
        if len(word) != 0:
            return(len(word[-1]))
        else:
            return 0
'''