class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        carry = 1
        # for i in range(len(digits) - 1, -1, -1):
        for i in range(len(digits)):
            if carry == 1:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                break
        
        if carry == 1:
            digits.append(1)

        digits.reverse()
        return digits            
        
