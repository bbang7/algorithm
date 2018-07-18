n = int(input('입력할 배열의 길이 : '))
N = tuple(map(int,input().split()))
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
    print(N,K,begin,end,middle)
    if N[middle] == K:
        return print(N[middle-1])
    else:
        if N[middle] > K:
            if begin == middle:
                if N[middle] > K:
                    return print('-1')
                else:
                    return print(N[middle-1])
            if middle == 0:
                return print(N[middle])
            else:
                return print('1'),floor(list,begin,middle-1,K)
        elif N[middle] < K:
            if middle == end:
                return print(N[middle])
            else:
                return print('2'),floor(list, middle + 1, end, K)


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
ceiling(N,begin,end,K)

floor(N,begin,end,K)





