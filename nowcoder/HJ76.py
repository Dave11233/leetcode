while True:
    try:
        n = int(input())
        arr = [str(i) for i in range(n ** 2 - n + 1, n ** 2 + n, 2)]
        print('+'.join(arr))
    except:
        break