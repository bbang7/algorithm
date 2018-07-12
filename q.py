import math

def mini():
    f = open('data.txt')
    data = f.read()
    f.close()


    N = int(input('입력될 정수의 개수를 입력하시오 : '))
    if N == -1:
        return print('프로그램을 종료합니다.')
    dlist = data.split('\n')
    nlist = []
    for i in range(0, N):
        nlist.append(int(dlist[i]))
    print('nlist = ',nlist)


    cmplist = []


    cmplist2 = []
    m = int(N**(1/2))
    s = 0
    for i in range(0, math.ceil(N/m)):
        room = []
        m = m*(i+1)
        print(m, s)
        for k in range(s, m):
            try:
                room.append(nlist[k])
            except IndexError:
                break
        print(room)
        cmplist2.append(min(room))

        m = int(N ** (1 / 2))
        s += m
    print('cmp2 = ', cmplist2)


    i, j = map(int, input('i 와 j 를 입력하시오 : ').split())
    if i > j:
        return {print('i값이 j 값보다 큽니다.'), mini()}
    print (i,j)

    i = i - 1
    j = j - 1
    iend = (i//m+1)
    jfir = (j//m-1)+1

    for a in range(i, iend*m):
        cmplist.append(nlist[a])
        # print('i',cmplist)

    for a in range(iend, jfir):
        cmplist.append(cmplist2[a])
        # print('m',cmplist)

    for a in range(jfir*m, j+2):
        cmplist.append(nlist[a])
        # print('j',cmplist)

    print('cmplist = ',cmplist)
    print('min = ', min(cmplist))



mini()

