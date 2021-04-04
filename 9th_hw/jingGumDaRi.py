def solution(distance, rocks, n): # distance = 거리 / rocks = 돌이 있는 위치를 담은 배열 / n = 제거할 돌의 수
    # 무작위로 주어진 돌 위치 배열 정렬
    rocks.sort()
    # 도착 지점의 거리 추가
    rocks.append(distance)
    # 시작점과 끝점 설정
    left, right = 0, distance
    
    # 탈출 조건
    while left <= right:
        # 시작 점은 항상 0
        prev = 0
        # 최소 값을 찾기 위해 우선 비교하기 전 최소 값을 비교할수 있는 가장 큰 값보다 크게 세팅
        minimum = 100000001
        # 기준 값 설정
        mid = (left + right) // 2
        # 기준 값 보다 거리가 짧은 돌은 제거하고 추가해주기
        removed = 0
        
        # 모든 돌 탐색
        for i in range(len(rocks)):
            # 현재 돌과 이전 돌을 비교해서 기준 값보다 짧으면 제거한 돌에 추가하기
            if rocks[i] - prev < mid:
                removed += 1
            # 그렇지 않다면 삭제하지 않고 최솟값 중 최댓 값을 찾기위해 확인
            else:
                minimum = min(minimum, rocks[i] - prev)
                # 이전 돌 한칸 전진
                prev = rocks[i]
        
        # 만약 제거된 돌이 제거하려고 했던 돌보다 많다면 기준 값을 더 작게 설정하기
        if removed > n:
            right = mid - 1
        # 만약 제거된 돌이 제거하려고 했던 돌보다 적다면 기준 값을 더 크게 설정하기
        else:
            left = mid + 1
            answer = minimum
            
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))