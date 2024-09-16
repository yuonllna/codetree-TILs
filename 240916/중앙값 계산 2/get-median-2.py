n = int(input())

org = list(map(int, input().split()))
sorted_part = []

for i in range(n):
    sorted_part.append(org[i])
    sorted_part.sort()  # 현재까지의 부분을 정렬
    
    if i % 2 == 0:  # 홀수 번째 입력일 때
        # 중간 값 출력
        print(sorted_part[i // 2], end=" ")