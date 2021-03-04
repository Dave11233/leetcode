import math
class Solution:
    def maxArea(self, height):
        max_value = -math.inf
        j = height.__len__() - 1
        i = 0
        while j >= i:
            max_value = max(max_value, (j - i)*(min(height[i], height[j])))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_value


if __name__ == '__main__':
    solution = Solution()
    x = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(x))
