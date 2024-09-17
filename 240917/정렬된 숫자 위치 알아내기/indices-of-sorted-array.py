class Sequence:
    def __init__(self, x, idx=0, flag = False):
        self.x = x
        self.idx = idx
        self.flag = flag

        
n = int(input())
org = list(map(int, input().split()))

seq = []
for i in range(n):
    seq.append(Sequence(org[i]))

seq.sort(key = lambda x:x.x)
for i in range(n):
    seq[i].idx = i+1

for i in range(n):
    for j in range(n):
        if org[i] == seq[j].x and seq[j].flag == False:
            print(seq[j].idx, end=" ")
            seq[j].flag = True
            break