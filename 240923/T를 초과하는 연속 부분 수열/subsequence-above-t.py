n, t = map(int, input().split())

arr = list(map(int, input().split()))

ans, cnt = 0, 0
for i in range(n):
	# Case 1
	if i >= 1 and arr[i] > t and arr[i-1] > t:
		cnt += 1
	# Case 2
	else:
		cnt = 1
	
	ans = max(ans, cnt)

print(ans)