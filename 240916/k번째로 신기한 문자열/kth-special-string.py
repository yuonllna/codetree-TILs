s = input()
arr = s.split(" ")
n = int(arr[0])
k = int(arr[1])
t = arr[2]

def is_same(str1, str2):
    for j in range(len(t)):
        if arr[i][j] != t[j]:
            return False
    return True

arr = [] 
for i in range(n):
    arr.append(input())

arr.sort()
cnt = 0
for i in range(n):
    if is_same(arr[i], t):
        cnt += 1
        if cnt == k:
            print(arr[i])