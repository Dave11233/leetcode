class Solution:

    def solve(self, n: int):
        m = n * n
        return str(m).endswith(str(n))


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(sum(map(Solution().solve, list(range(n + 1)))))
        except EOFError:
            break
