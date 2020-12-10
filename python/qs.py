"""
Quick Select 
"""
from random import randint

def partition(arr, start, end, pivot_index):
    arr[end],arr[pivot_index] = arr[pivot_index],arr[end]
    pivot = arr[end]
    i = j = start
    while i < end:
        if arr[i] <= pivot:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        i+=1

    arr[j],arr[end]=arr[end],arr[j]
    print('\t' + ''.join([('  {} '.format(arr[i]) if i != j else '|{}| '.format(arr[i])) for i in range(len(arr))]).strip())
    print()
    return j

def quick_select(arr, k, start, end):
    if start > end:
        return

    pivot = randint(start, end)
    print('Pivot is: {}'.format(arr[pivot]))
    print('Arr is: ' + ' '.join(str(item) for item in arr))
    pivot_index = partition(arr, start, end, pivot)
    if pivot_index==len(arr)-k:
        return arr[pivot_index]
    elif pivot_index < len(arr)-k:
        return quick_select(arr, k, pivot_index+1, end)
    else:
        return quick_select(arr, k, start, pivot_index-1)

def kth_largest(arr, k):
    return quick_select(arr, k, 0, len(arr)-1)

print(kth_largest([1094, 19, 33, 33, 2, -1], 1)) # 1094