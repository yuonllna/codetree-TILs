n, m = tuple(map(int, input().split()))
arr = [[0] * n for _ in range(n)]

cnt = 0
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r-1][c-1] = 1
    if r-2 >= 0 and arr[r-2][c-1] == 1:
        cnt += 1
    if r < n and arr[r][c-1] == 1:
        cnt += 1
    if c-2 >= 0 and arr[r-1][c-2] == 1:
        cnt += 1
    if c < n and arr[r-1][c] == 1:
        cnt += 1
    if cnt >= 3:
        print(1)
    else: print(0)
    cnt = 0