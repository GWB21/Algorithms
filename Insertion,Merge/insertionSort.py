import random


class Sorter:
    def __init__(self, arr):
        # 배열을 클래스 속성으로 초기화
        self.arr = arr

    def insertion_sort_iterative(self):
        # 반복 방식 삽입 정렬
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def insertion_sort_recursive(self, n):
        # 재귀 방식 삽입 정렬
        if n <= 1:  # 기저 조건: 배열 크기가 1 이하면 정렬할 필요 없음
            return

        # 앞부분(n-1)을 재귀적으로 정렬
        self.insertion_sort_recursive(n - 1)

        # 마지막 요소를 앞의 정렬된 부분에 삽입
        key = self.arr[n - 1]
        j = n - 2
        while j >= 0 and self.arr[j] > key:
            self.arr[j + 1] = self.arr[j]
            j -= 1
        self.arr[j + 1] = key


# 무작위 배열 생성 (1~100 사이의 숫자 10개)
random_arr = [random.randint(1, 100) for _ in range(10)]

# 객체 생성 및 정렬 테스트
sorter = Sorter(random_arr.copy())
print("Original array:", sorter.arr)

# 반복 방식으로 정렬
sorter.insertion_sort_iterative()
print("Sorted iteratively:", sorter.arr)

# 배열 다시 초기화 후 재귀 방식으로 정렬
sorter = Sorter(random_arr.copy())
sorter.insertion_sort_recursive(len(sorter.arr))
print("Sorted recursively:", sorter.arr)