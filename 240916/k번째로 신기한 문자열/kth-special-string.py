s = input()
arr = s.split(" ")
n = int(arr[0])
k = int(arr[1])
t = arr[2]

arr = [] 
for i in range(n):
    arr.append(input())

cnt1 = 0
arr.sort()
for i in range(n):
    cnt2 = 0
    for j in range(0,len(t)):
        if arr[i][j] == t[j]:
            cnt2 += 1
    if cnt2 == len(t):
        cnt1 += 1
        if(cnt1 == k): 
            print(arr[i])
            break
    else: continue