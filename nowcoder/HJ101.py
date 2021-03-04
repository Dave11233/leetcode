while True:
    try:
        n = input()
        data = list(map(int, input().split()))
        flag = int(input())
        data.sort(reverse=True if flag == 0 else False)
        print(" ".join([str(i) for i in data]))
    except EOFError:
        break