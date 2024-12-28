# import random
#
#
# def randomized_quick_sort(arr, start, end):
#     if start < end:
#         # Partition 단계: 피벗 위치를 계산
#         pivot_index = randomized_partition(arr, start, end)
#         # 피벗 기준으로 좌우 부분 배열 정렬 수행
#         randomized_quick_sort(arr, start, pivot_index - 1)
#         randomized_quick_sort(arr, pivot_index + 1, end)
#
#
# def randomized_partition(arr, start, end):
#     # 랜덤으로 피벗 선택
#     pivot_index = random.randint(start, end)
#     pivot = arr[pivot_index]
#     arr[pivot_index], arr[end] = arr[end], arr[pivot_index]  # 선택된 피벗을 끝으로 이동 => its the key!
#     target = start - 1
#
#     for j in range(start, end):
#         if arr[j] <= pivot:
#             target += 1
#             arr[target], arr[j] = arr[j], arr[target]  # 작은 값을 왼쪽으로 이동
#     arr[target + 1], arr[end] = arr[end], arr[target + 1]  # 피벗을 제자리로 이동
#     return target + 1
#
#
# # 사용 예시
# arr = [2, 8, 7, 1, 3, 5, 6, 9]
# randomized_quick_sort(arr, 0, len(arr) - 1)
# print("정렬된 배열:", arr)



import random

def random_quick_sort(arr, start, end):
    if start < end:
        pivot_i = partition(arr,start, end)
        random_quick_sort(arr, start, pivot_i - 1)
        random_quick_sort(arr, pivot_i + 1, end)

def partition(arr, start, end):
    target = start - 1
    pivot_i = random.randint(start, end)
    arr[end], arr[pivot_i] = arr[pivot_i], arr[end]

    for i in range(start, end):
        if arr[i] <= arr[end]:
            target += 1
            arr[i], arr[target] = arr[target], arr[i]
    arr[target + 1], arr[end] = arr[end], arr[target + 1]

    return target + 1

arr1 = [2, 4, 6, 8, 9, 1, 3, 5, 7]
random_quick_sort(arr1, 0, len(arr1) - 1)
print(arr1)


































