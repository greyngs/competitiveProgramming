class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = len(height) - 1
        left = 0
        water = 0

        while right > left:
            water = max(water, min(height[left], height[right]) * (right - left))

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        
        return water

        # water = 0
        # for i in range(len(height)):
        #     for j in range(i):
        #         area = min(height[i], height[j]) * (i - j)
        #         if area > water:
        #             water = area
        # return water

