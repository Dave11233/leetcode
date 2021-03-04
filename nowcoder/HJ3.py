while True:
    try:
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(int(input()))
        arr = set(arr)
        for i in sorted(arr):
            print(i)
    except:
        break