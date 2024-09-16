class Data:
    def __init__(self, date, days, wth):
        self.date = date
        self.days = days
        self.wth = wth

n = int(input())
data = []
for i in range(n):
    date, days, wth = tuple(input().split())
    data.append(Data(date, days, wth))

data.sort(key=lambda data: data.date)

for i in range(n):
    if data[i].wth == "Rain":
        print(f"{data[i].date} {data[i].days} {data[i].wth}")
        break