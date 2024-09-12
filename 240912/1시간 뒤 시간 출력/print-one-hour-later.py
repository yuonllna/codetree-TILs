time = input()
arr = time.split(":")
hour = int(arr[0]) + 1
min = int(arr[1])

print(f"{hour}:{min}")