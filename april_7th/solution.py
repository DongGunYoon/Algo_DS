def solution(words, queries):
    result = [0] * len(queries)
    
    for i in range(len(queries)):
        count = queries[i].count('?')
        length = len(queries[i])
        ind = queries[i].index('?')
        sum = 0

        for word in words:
            if len(word) != length:
                continue
            elif ind == 0:
                if word[count:] == queries[i][count:]:
                    sum += 1
            else:
                if word[:ind] == queries[i][:ind]:
                    sum += 1
    
            result[i] = sum

    return result