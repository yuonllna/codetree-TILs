a = input()
arr = a.split(" ")
n = int(arr[0])
m = int(arr[1])

def gcd(n, m):
    ans = 0
    for i in range(1, min(n, m)):
        if(n % i == 0 and m % i == 0):
            ans = i
    print(ans)

gcd(n, m)