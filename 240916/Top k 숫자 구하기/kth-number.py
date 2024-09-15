n, k = map(int, input().split())

arr = list(map(int, input().split()))

if 0 <= k < n:  # k가 0 이상 n보다 작은지 확인
    arr.sort()
    print(arr[k])
else:
    print("Invalid index")