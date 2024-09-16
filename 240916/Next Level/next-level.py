class NextLevel:
    def __init__(self, id_="codetree", lv=10):
        self.id_ = id_
        self.lv = lv

u_id, u_lv = tuple(input().split())
usr1 = NextLevel()
usr2 = NextLevel(u_id, u_lv)

print(f"user {usr1.id_} lv {usr1.lv}")
print(f"user {usr2.id_} lv {usr2.lv}")