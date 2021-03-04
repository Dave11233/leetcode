from typing import List

class Solution:
    def coordinateMoving(self, cmd: List[str]) -> List[int]:
        if not cmd:
            return [0, 0]
        ans = [0, 0]
        for item in cmd:
            if item.startswith("A"):
                step = item[1:]
                if step.isdigit():
                    step = int(step)
                    ans[0] -= step
            elif item.startswith("D"):
                step = item[1:]
                if step.isdigit():
                    step = int(step)
                    ans[0] += step
            elif item.startswith("W"):
                step = item[1:]
                if step.isdigit():
                    step = int(step)
                    ans[1] += step
            elif item.startswith("S"):
                step = item[1:]
                if step.isdigit():
                    step = int(step)
                    ans[1] -= step
            else:
                continue
        return ans


if __name__ == '__main__':
    cmds = input()
    result = [str(item) for item in Solution().coordinateMoving(cmds.split(";"))]
    print(",".join(result))