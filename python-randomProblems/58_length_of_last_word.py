class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        s = s.strip()
        words = s.split(" ")
        return len(words[-1])
        """
        count = 0
        flag = False
        
        for i in s:
            if i !=' ' and flag == False:
                count += 1
            elif i !=' ' and flag == True:
                count = 1
                flag = False
            else:
                flag = True

        return count                          

