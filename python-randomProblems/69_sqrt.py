class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
    
        left = 1
        right = x
        
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result

        # super inefficient but works good with low numbers
        # if x == 0 or x == 1:
        #     return x
        # elif x == 2:
        #     return 1
            
        # for i in range(x):
        #     if i*i > x:
        #         return i-1         
        