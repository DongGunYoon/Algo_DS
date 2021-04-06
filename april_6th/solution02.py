def solution(money):
    d = [0] * len(money)
    d[0] = money[0]
    d[1] = max(d[0], money[1])
    
    for i in range(2, len(money)):
        d[i] = max(d[i-1], d[i-2] + money[i])
    
    return d[len(money) - 2]

'''
4월 6일

정확성: 20.0
효율성: 35.0
합계: 55.0 / 100.0
'''
