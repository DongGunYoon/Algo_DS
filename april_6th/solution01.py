import sys
sys.setrecursionlimit(60001)

memo = {1: 1, 2: 2}

def solution(n):
    if n in memo:
        return memo[n]

    answer = solution(n-1) + solution(n-2)
    memo[n] = answer
    return answer % 1000000007