class Info:
    def __init__(self, name, num, region):
        self.name = name
        self.num = num
        self.region = region

n = int(input())
infos = []
for i in range(n):
    name, num, region = tuple(input().split())
    infos.append(Info(name, num, region))

infos.sort(key=lambda info: info.name)

print(f"name {infos[n-1].name}")
print(f"addr {infos[n-1].num}")
print(f"city {infos[n-1].region}")