s = input()
arr = s.split(" ")
n = int(arr[0])
k = int(arr[1])
ap = arr[2]

arr = [] 
for i in range(n):
    arr.append(input())

cnt = 0
arr.sort()
for i in range(n):
    if arr[i][0] == 'a' and arr[i][1] == 'p':
        cnt += 1
        if(cnt == k): 
            print(arr[i])
            break
    else: continue