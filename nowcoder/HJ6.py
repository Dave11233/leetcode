class Solution:

    def solve(self, n):
        if n <= 3:
            return [n]
        ret = []
        a = 2
        while a * a <= n:
            while n % a == 0:
                ret.append(str(a))
                n = n // a
            a += 1
        if n > 1:
            ret.append(str(n))
        return ret


if __name__ == '__main__':
    n = int(input())
    ans = Solution().solve(n)
    print(" ".join(ans) + " ")