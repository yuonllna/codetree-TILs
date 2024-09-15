n = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()
cnt = 0
for i in range(n):
    if arr1[i] == arr2[i]:
        cnt += 1

if(cnt == n):
    print("Yes")
else: print("No")