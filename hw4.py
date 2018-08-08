import random
import time

def bubble_sort(list):
    for start_index in range(len(list) - 1):
        for index in range(1, len(list) - start_index):
            if list[index - 1] > list[index]:
                list[index], list[index-1] = list[index-1],list[index]
    return list


def selection_sort(list):
    for sel in range(len(list)-1):
        min = list[sel]
        minindex = sel

        for step in range(sel+1, len(list)):
            if min > list[step]:
                min = list[step]
                minindex = step

        list[minindex] = list[sel]
        list[sel] = min
    return list

def insertion_sort(list):
    list.insert(0, -1)
    for start_index in range(2, len(list)):
        temp = list[start_index]
        insert_index = start_index

        while list[insert_index-1] > temp:
            list[insert_index] = list[insert_index-1]
            insert_index = insert_index - 1

        list[insert_index] = temp
    del list[0]
    return  list


def merge_sort(list):
    if len(list) <= 1:
        return list

    left = merge_sort(list[:len(list)//2])
    right = merge_sort(list[len(list)//2:])

    i, j, k = 0, 0, 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j<len(right):
            list[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i<len(left):
            list[k] = left[i]
            i += 1
            k += 1
    return list


def quick_sort(list,piv):
    length = len(list)
    if(length <= 1):
        return list
    else:
        p = list[piv]
        up = [sel for sel in list if sel > p]
        same = [sel for sel in list if sel == p]
        down = [sel for sel in list if sel < p]

        return quick_sort(down,0) + same + quick_sort(up,0)


def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted



list = []
for i in range(8):
    line1,line2,line3,line4,line5,line6= [],[],[],[],[],[]

    for i in range(1000):
        line1.append(random.randint(1, 1000))
        line2.append(random.randint(1, 1000))
    line2.reverse()

    for i in range(10000):
        line3.append(random.randint(1, 10000))
        line4.append(random.randint(1, 10000))
    line4.reverse()

    for i in range(100000):
        line5.append(random.randint(1, 100000))
        line6.append(random.randint(1, 100000))
    line6.reverse()

    list.append(line1)
    list.append(line2)
    list.append(line3)
    list.append(line4)
    list.append(line5)
    list.append(line6)

print('                        Random1000                  Reverse1000                   Random10000                 Reverse10000                        Random100000                        Reverse100000     ')
print('Bubble   ',end='')
for i in range(0,4):
    start = time.time()
    bubble_sort(list[i])
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Selection',end='')
for i in range(6,10):
    start = time.time()
    selection_sort(list[i])
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Insertion',end='')
for i in range(12,16):
    start = time.time()
    insertion_sort(list[i])
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Merge    ',end='')
for i in range(18,22):
    start = time.time()
    merge_sort(list[i])
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Quick1   ',end='')
for i in range(24,28):
    start = time.time()
    quick_sort(list[i],-1)
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Quick2   ',end='')
for i in range(30,34):
    start = time.time()
    quick_sort(list[i],len(list)//2)
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Quick3   ',end='')
for i in range(36,40):
    start = time.time()
    quick_sort(list[i],random.randint(1,len(list)))
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')


print('Heap     ',end='')
for i in range(42,46):
    start = time.time()
    heap_sort(list[i])
    end = time.time()
    elapsed = end - start
    print('     ',elapsed,end='     ')
print()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
