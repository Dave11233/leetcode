from typing import Tuple


class Solution:

    def solve(self, s: str) -> Tuple[int, int, int]:
        if not s:
            return 0, 0, 0
        eng_counter = 0
        space_counter = 0
        digit_counter = 0
        other_counter = 0

        for i in s:
            if i.isalpha():
                eng_counter += 1
            elif i.isdigit():
                digit_counter += 1
            elif i == " ":
                space_counter += 1
            else:
                other_counter += 1
        return space_counter, eng_counter, digit_counter, other_counter


if __name__ == '__main__':
    while True:
        try:
            S = input()
            space_counter, eng_counter, digit_counter, other_counter = Solution().solve(S)
            print(eng_counter)
            print(space_counter)
            print(digit_counter)
            print(other_counter)
        except EOFError:
            break