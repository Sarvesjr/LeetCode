class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        l,r = 0, len(height)-1

        while(l<r):
            h = min(height[l],height[r])
            w = r-l
            area=w*h
            water=max(water,area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return water