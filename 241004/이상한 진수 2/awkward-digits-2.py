arr = list(map(int, input()))

max_num = 0
for i in range(len(arr)):
    sum = 0
    if arr[i] == 1:
        arr[i] = 0
        for j in range(len(arr)):
            sum += 2**(len(arr)-j-1) if arr[j] == 1 else 0
        max_num = max(max_num, sum)
        arr[i] = 1

    else:
        arr[i] = 1
        for j in range(len(arr)):
            sum += 2**(len(arr)-j-1) if arr[j] == 1 else 0
        max_num = max(max_num, sum)
        arr[i] = 0

print(max_num)