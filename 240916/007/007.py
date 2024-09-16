class Info:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time
    
s = input()
arr = s.split(" ")
c = arr[0]
p = arr[1]
t = arr[2]

info = Info(c,p,t)
print(f"secret code : {info.code}")
print(f"meeting point : {info.point}")
print(f"time : {info.time}")