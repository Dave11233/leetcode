def solve(s: str):
    if not s:
        return ""
    ans = ""
    i, j = 0, 0
    length = len(s)
    while i < length:
        if s[i].isdigit():
            ans += "*"
            j = i + 1
            while j < length and s[j].isdigit():
                j += 1
            ans += s[i:j]
            ans += "*"
            i = j
        else:
            ans += s[i]
            i += 1
    return ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            print(solve(s))
        except EOFError:
            break
