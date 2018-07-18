n = int(input('입력할 배열의 길이 : '))
N = tuple(map(int,input().split()))
N.sort()
K = int(input('K 를 입력하시오 : '))

begin = 0
end = len(N)
count = 0

def sol(list,begin,end, K ,count):
    N = list
    K = K
    begin = begin
    end = end
    count = count
    for i in range(begin,end):
        if begin == end-1:
            return print('순서쌍 개수 : ',count)
        if begin == i:
            continue
        elif N[begin]+N[i] == K:
            return sol(N, begin + 1, end, K, count + 1)
        elif end-1 == i:
            return sol(N, begin + 1, end, K, count)
sol(N,begin,end,K,count)