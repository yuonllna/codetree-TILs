n = int(input()) 
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
sum = 0
for i in range(n):
    for j in range(n):
        if i-1 >= 0 and arr[i-1][j] == 1:
            cnt += 1
        if i+1 < n and arr[i+1][j] == 1:
            cnt += 1
        if j-1 >= 0 and arr[i][j-1] == 1:
            cnt += 1
        if j+1 < n and arr[i][j+1] == 1:
            cnt += 1
        if cnt >= 3:
            sum += 1
        cnt = 0
    
print(sum)