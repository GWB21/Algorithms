memo = [0 for i in range(100)]

# def fibonacci_recuresive_use_array(n):
#     if n <= 1:
#         return n
#     if memory[n] != 0:
#         return memory[n]
#     memory[n] = fibonacci_recuresive_use_array(n-1) + fibonacci_recuresive_use_array(n-2)
#     return memory[n]
#
# def fibonacci_recursive_use2_variables(n, prev2=0, prev1=1):
#     if n <= 0:
#         return prev2
#     if n == 1:
#         return prev1
#
#     return fibonacci_recursive_use2_variables(n-1, prev1, prev1 + prev2)
#
# def fibonacci_iterative_use_two_variables(n):
#     if n <= 0:
#         return 0
#     if n <= 2:
#         return 1
#
#     prev2 = 1
#     prev1 = 1
#     for i in range(2, n+1):
#         prev2, prev1 = prev1, prev1 + prev2
#     return prev1
#
# print(fibonacci_iterative_use_two_variables(2))

def fib(n):
    if memo[n] != 0:
        return memo[n]
    elif n == 1 or n == 2: #base case
        return 1
    else:
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]

def fib_iterative(n):
    if n==1 or n==2:
        return 1
    else:
        a,b=1,1
        for i in range(1, n-2):
            b,a = a, a+b
        return a+b
print(fib(8))
print(fib_iterative(20))


