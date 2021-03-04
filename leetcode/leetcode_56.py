from collections import deque


class Solution:
    def merge(self, intervals):
        if not intervals:return []
        intervals_ = list(sorted(intervals,key=lambda x:x[0]))
        d = deque()
        d.append(intervals_[0])
        length = len(intervals_)
        for i in range(1,length):
            x = d[-1]
            x_ = intervals_[i]
            if x[0] <= x_[0] <= x[1] <= x_[1]:
                x[1] = x_[1]
                d.pop()
                d.append(x)
            elif x[0] <= x_[0] <= x_[1] <= x[1]:
                pass
            else:
                d.append(x_)

        return list(d)


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1,4],[2,3]]))