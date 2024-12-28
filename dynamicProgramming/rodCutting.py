def rod_cutting(n):
    # 메모이제이션: 이미 계산한 값이 있으면 반환
    if n in memo:
        return memo[n]

    # Base case: 남은 길이가 0인 경우
    if n == 0:
        return 0

    result = []  # 가능한 결과를 저장할 배열 초기화

    # 가능한 모든 길이를 순회하며 최대값 계산
    for i in range(1, len(prices) + 1):
        if i <= n:  # 남은 길이보다 작거나 같은 경우에만
            result.append(prices[i - 1] + rod_cutting(n - i))  # 값 추가

    memo[n] = max(result)  # 최댓값을 저장
    return memo[n]


# Global variable
prices = [1, 5, 8, 9, 10]  # 각 길이별 가격
memo = {}  # 메모이제이션 딕셔너리

print("Maximum profit:", rod_cutting(len(prices)))