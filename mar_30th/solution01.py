'''
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
입출력 예
'''

# 문제 1

def solution(s):
    # 문자열로 주어진 값들을 담을 리스트 생성
    arr = []
    
    # 공백으로 구분된 숫자들을 순서대로 리스트에 삽입
    for num in s.split(' '):
        arr.append(int(num))

    # 최소값과 최대값을 찾기위해 정렬
    arr.sort()

    # 졍렬된 리스트의 양측 마지막 인덱스를 순서대로 출력
    answer = str(arr[0]) + ' ' + str(arr[-1])
    
    return answer

# 문제 1 #Test_Case

print(solution("-1 2 3 5 3 2 9 -9 -10 2"))

print(solution("1 8 3 229 -1 -55 3 2"))
