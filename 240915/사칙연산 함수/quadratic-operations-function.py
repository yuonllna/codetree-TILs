inp = input()

arr = inp.split(" ")
a = int(arr[0])
op = arr[1]
b = int(arr[2])

if op == '+':
    print(f"{inp} = {a+b}")

elif op == '-':
    print(f"{inp} = {a-b}")

elif op == '*':
    print(f"{inp} = {a*b}")

elif op == '/':
    print(f"{inp} = {a//b}")

else: print(False)