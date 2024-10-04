r, c = input().split()
arr = [list(input().split()) for _ in range(r)]

max_cnt = 0
for i in range(r):
    for j in range(c - 1):
        for k in range(i + 1, r):
            cnt = 0
            for l in range(c - 1):
                if arr[i][j] != arr[l][k]:
                    cnt += 1

print(cnt)