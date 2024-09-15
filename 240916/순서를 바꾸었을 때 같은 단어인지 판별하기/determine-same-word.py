s1 = input()
s2 = input()
list1 = list(s1)
list2 = list(s2)

list1.sort()
list2.sort()

if len(list1) != len(list2):
    print("No")
elif list1 == list2:
    print("Yes")
else: print("No")