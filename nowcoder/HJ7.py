class Solution:
    def solve(self, x:float) -> int:
        x_next = x - int(x)
        x_next = int(x_next*10)
        if x_next >= 5:
            return int(x+1)
        else:
            return int(x)


if __name__ == '__main__':
    x = float(input())
    print(Solution().solve(x))
