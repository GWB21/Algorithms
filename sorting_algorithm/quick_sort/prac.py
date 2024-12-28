import random


def quicksort(arr,start,end):
    if start <= end:
        pivot = partition(arr,start,end)
        quicksort(arr,start,pivot-1)
        quicksort(arr,pivot+1, end)


def partition(arr,start,end):
    pivot = end
    right = start - 1

    for i in range(start,end):
        if i <= arr[pivot]:
            arr[i], arr[right] = arr[right], arr[i]
            right += 1

    arr[right + 1], arr[pivot] = arr[pivot], arr[right + 1]
    return right + 1

arr = [random.randint(0,100) for x in range(10)]
print(quicksort(arr,0,len(arr)-1))