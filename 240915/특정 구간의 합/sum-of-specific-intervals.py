n, m = map(int, input().split())
arr = list(map(int, input().split(" ")))

def func(n, m, arr):
    for _ in range(0, m):
        a1, a2 = map(int, input().split(" "))
        sum = 0 
        for i in range(a1-1, a2):
            sum += arr[i]
        print(sum)

func(n, m, arr)