"""
10
1 2 3 4 5 6 7 8 9 10
11

25
1 3 6 9 13 17 21 23 24 31 37 38 44 45 47 51 55 58 71 73 88 91 99 102
72

40
1 17 19 23 25 28 41 44 49 50 61 64 65 67 71 77 79 81 82 83 84 90 91 92 96 99 101 103 109 121 128 132 133 150 152 161 165 167 177 178
111
"""

n = int(input('입력할 배열의 길이 : '))
N = list(map(int,input().split()))
N.sort()
K = int(input('K 를 입력하시오 : '))

begin = 0
end = len(N)-1

def floor(list,begin,end, K):
    N = list
    K = K
    begin = begin
    end = end
    middle = (begin+end)//2
    if N[middle] == K:
        return print(N[middle-1])
    else:
        if N[middle] > K:
            if end == middle:
                if N[middle] > K:
                    return print(N[middle-1])
                else:
                    return print('-1')
            if middle == 0:
                return print('-1')
            else:
                return floor(list, begin, middle-1, K)

        elif N[middle] < K:
            if end == middle:
                try:
                    if N[middle] < K:
                        return print(N[middle])
                except:
                    return print('-1')
                else:
                    return print('-1')

            else:
                return floor(list,middle+1,end,K)


def ceiling(list,begin,end, K):
    N = list
    K = K
    begin = begin
    end = end
    middle = (begin+end)//2
    if N[middle] == K:
        return print(N[middle+1])
    else:
        if N[middle] > K:
            if begin == middle:
                if N[middle] < K:
                    return print('-1')
                else:
                    return print(N[middle])
            if middle == 0:
                return print(N[middle])
            else:
                return ceiling(list, begin, middle-1, K)

        elif N[middle] < K:
            if end == middle:
                try:
                    if N[middle] < K:
                        return print(N[middle+1])
                except:
                    return print('-1')
                else:
                    return print('-1')

            else:
                return ceiling(list,middle+1,end,K)

floor(N,begin,end,K)
ceiling(N,begin,end,K)





