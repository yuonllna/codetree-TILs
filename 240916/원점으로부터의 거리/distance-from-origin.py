class Coordinate:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

        
n = int(input())
coordinates = []
for i in range(n):
    x, y = tuple(input().split())
    coordinates.append(Coordinate(int(x), int(y), i+1))


coordinates.sort(key=lambda x: (abs(x.x + x.y), x.num))

for coordinate in coordinates:
   print(coordinate.num)