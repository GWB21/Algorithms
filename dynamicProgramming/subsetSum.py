# def subset_sum_memo(set, n, target_sum, memo):
#     # Base cases
#     if target_sum == 0:
#         return True
#     if n == len(set):
#         return False
#
#     # Check if the result is already computed
#     if (n, target_sum) in memo:
#         return memo[(n, target_sum)]
#
#     # If the current element is greater than the target sum, ignore it
#     if set[n] > target_sum:
#         result = subset_sum_memo(set, n+1, target_sum, memo)
#     else:
#         # Check if the target sum can be obtained by:
#         # (1) including the current element
#         # (2) excluding the current element
#         result = (subset_sum_memo(set, n+1, target_sum, memo) or
#                   subset_sum_memo(set, n+1, target_sum-set[n], memo))
#
#     # Store the result in the memo dictionary
#     memo[(n, target_sum)] = result
#     return result
#
# # Example usage
# set = [3, 34, 4, 12, 5, 2]
# target_sum = 21
# memo = {}
# print("Subset with sum", target_sum, "exists:", subset_sum_memo(set, 0, target_sum, memo))

arrList = [3, 4, 3, 1]
memo = {}
def subset_sum(n = 0, target_sum = 0):
    # 메모 확인
    if (n, target_sum) in memo:
        return memo[(n, target_sum)]

    # Base Case 1: 부분합을 찾았을 때
    if target_sum == 0:
        return True

    # Base Case 2: 끝까지 탐색했으나 부분합 발견 못 함
    if n == len(arrList):
        return False

    # 포함 / 미포함을 조건적으로 처리
    result = (subset_sum(n + 1, target_sum) or
              (subset_sum(n + 1, target_sum - arrList[n]) if target_sum >= arrList[n] else False))

    # 결과 저장
    memo[(n, target_sum)] = result
    return result

# 실행 예제
print(subset_sum(target_sum=6))  # True