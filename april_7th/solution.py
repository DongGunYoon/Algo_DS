from bisect import bisect_left, bisect_right

def solution(words, queries):
    result = []

    for i in range(len(queries)):
        count = queries[i].count('?')
        length = len(queries[i])
        sum = 0
        ind = queries[i].index('?')
        if ind == 0:
            for word in words:
                if word[count:] == queries[i][count:] and length == len(word):
                    sum += 1
            result.append(sum)
        else:
            for word in words:
                if word[:ind] == queries[i][:ind] and length == len(word):
                    sum += 1
            result.append(sum)

    return result