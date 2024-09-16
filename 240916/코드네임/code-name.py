class Agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

agent = []
for i in range(5):
    name, score = tuple(input().split())
    agent.append(Agent(name, int(score)))

min = 100
idx = 0
for i in range(5):
    if min > agent[i].score:
        min = agent[i].score
        idx = i
    
print(f"{agent[idx].code_name} {agent[idx].score}")