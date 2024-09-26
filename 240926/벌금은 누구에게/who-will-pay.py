n, m, k = tuple(map(int,input().split()))

stu = [0] * 1000001
ans = [-1] * 1000001
idx = 0
for _ in range(m):
    num = int(input())
    stu[num] += 1
    if stu[num] >= k:
        ans[idx] = num
        idx += 1

if ans[0] == -1:
    print(-1)
else:
    print(ans[0])