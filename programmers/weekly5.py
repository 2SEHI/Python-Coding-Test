## 문제 풀이 : https://2sehi.github.io/programming%20test/54_Programming_Test/
def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    word_dict = []
    from itertools import product

    for i in range(1, len(alphabet)+1):
        result = list(map(lambda x: ''.join(x), list(product(alphabet, repeat=i))))
        for j in result :
            word_dict.append(j)

    word_dict.sort()
    return word_dict.index(word)+1

word = 'AAAAE'
print(solution(word))