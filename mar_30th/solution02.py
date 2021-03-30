
# 문제 2

'''
문제 설명
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
'''

from collections import deque

def solution(priorities, location): 
    
    # 큐에 priorities삽입
    queue = deque(priorities) 
    # 출력 순서를 나타낼 counter 변수 생성
    counter = 0 

    while queue:
        # 출력 순위가 가장 높은 큐 확인
        max_value = max(queue) 

        # 현재 큐에서 location이 0인 값 확인
        value = queue.popleft() 
        
        # 현재 값이 가장 큰 값일때 카운터 + 1
        if value == max_value: 
            counter += 1 
            # 원하는 location값이면 break후 카운터 값 출력
            if location == 0: 
                break 
            # 만약 location값이 원하는게 아니라면 한 칸 당기기
            else: 
                location -= 1 

        else: 
            # 값이 우선순위가 가장 크지 않을때 큐에 제일 뒤로 보내기
            queue.append(value) 

            # 만약 해당 값이 로케이션일때 큐의 제일 뒤로 location위치 옮기기
            if location == 0: 
                location = len(queue) - 1 
            # 만약 해당 값이 원하는 로케이션이 아니면 한칸 당기기
            else: 
                location -= 1 
                
    # counter 값 출력하기
    return counter


print(solution_02([1, 1, 9, 1, 1, 1], 0))