class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        x = [[A, C], [E, G]]
        x.sort(key=lambda t: t[0])
        x_ = 0
        if x[0][0] <= x[1][1] <= x[0][1]:
            x_ = min(x[0][1], x[1][1]) - max(x[0][0], x[1][0])
        if x_ == 0:
            return s1 + s2
        y = [[B, D], [F, H]]
        y.sort(key= lambda t:t[0])
        y_ = 0
        if y[0][0] <= y[1][1] <= y[0][1]:
            y_ = min(y[0][1], y[1][1]) - max(y[0][0], y[1][0])
        if y_ == 0:
            return s1 + s2
        return s1+s2-x_*y_


