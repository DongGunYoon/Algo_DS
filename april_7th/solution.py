def solution(words, queries):
    result = [0] * len(queries)
    
    for i in range(len(queries)):
        count = queries[i].count('?')
        ind = queries[i].index('?')

        for word in words:
            if len(word) != len(queries[i]):
                continue
            elif ind == 0:
                if word[count:] == queries[i][count:]:
                    result[i] += 1
            else:
                if word[:ind] == queries[i][:ind]:
                    result[i] += 1

    return result